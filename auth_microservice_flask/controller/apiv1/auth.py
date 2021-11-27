from time import time
from flask import request
from jwt import encode

from authman.authman import db
from authman.config import Config
from authman.model import User
from authman.schema.apiv1 import UserSchema
from authman.util import jsonify, now

class AuthController:

    def verify_jwt_token():
        return jsonify(status=501, code=107)

    def create_jwt_token():
        if request.is_json is False:
            return jsonify(status=415, code=101)
        user_schema = UserSchema(only=["username", "password"])
        try:
            data = user_schema.load(request.get_json()) # Request validation.
        except:
            return jsonify(status=400, code=104)
        if not data["username"] or not data["password"]:
            return jsonify(status=400, code=105)
        try:
            user = User.query.filter_by(username=data["username"]).first()
        except:
            return jsonify(status=500, code=102) # Database error.
        if user is None:
            return jsonify(status=401, code=103)
        if user.expires_at < now():
            return jsonify(status=401, code=108)
        if user.status != 3:
            if user.status == 0:
                return jsonify(status=401, code=118)
            if user.status == 1:
                return jsonify(status=401, code=119)
            if user.status == 2:
                return jsonify(status=401, code=120)
        if user.password != data["password"]:
            user.failed_auth_at = now()
            user.failed_auth_count += 1
            try:
                db.session.commit()
            except:
                db.seesion.rollback()
                return jsonify(status=500, code=102) # Database error.
            return jsonify(status=401, code=111)
        try:
            jwt_token = encode(
                {
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "role": user.role
                    },
                    "sub": user.id,
                    "nbf": time(),
                    "exp": time() + Config.USER_DEFAULT_TOKEN_EXPIRY_TIME,
                },
                Config.SECRET_KEY,
                algorithm=Config.USER_DEFAULT_TOKEN_ALGO
            ).encode("utf8")
        except:
            return jsonify(status=500, code=110)
        user.last_login_at = now()
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102) # Database error.
        user_schema = UserSchema()
        return jsonify(
            {"user": user_schema.dump(user)},
            status=201,
            headers={
                "X-Subject-Token": jwt_token
            }
        )
