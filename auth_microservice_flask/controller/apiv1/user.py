from flask import request
from auth_microservice_flask.util  import jsonify, now, user_expires_at
from auth_microservice_flask.auth_microservice_flask import db
from auth_microservice_flask.model  import User
from auth_microservice_flask.schema.apiv1  import UserSchema

class UserController:
    
    def get_users():
        users_schema = UserSchema(many=True)
        try:
            users = User.query.all()
        except:
            return jsonify(status=500, code=102)
        return jsonify(
            {"users": users_schema.dump(users)} # list of user
        )

    def get_user(user_id):
        user_schema = UserSchema()
        try:
            user = User.query.get(user_id)
        except:
            return jsonify(status=500, code=102)
        if user is None:
            return jsonify(status = 404, code = 103) #Not Found
        return jsonify({"user": user_schema.dump(user)}) # single user

    def create_user():
        if not request.is_json:
            return jsonify(status=415, code=101)
        
        user_schema = UserSchema(only=["username", "password"])
        try:
            data = user_schema.load(request.get_json())
        except:
            return jsonify(status=400, code=104)
        if not data["username"] or not data["password"]:
            return jsonify(status=400, code=105)
        try:
            user = User.query.filter_by(username=data["username"]).first()
        except:
            return jsonify(status=500, code=102)
        if user is not None:
            return jsonify(status=409, code=106)
        
        user = User(username=data["username"], password=data["password"])
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)
        user_schema = UserSchema()
        return jsonify({"user": user_schema.dump(user)}, status=201, )
    def update_user(user_id):
        if not request.is_json:
            return jsonify(status=415, code=101)
        user_schema = UserSchema(only=["password"])
        try:
            data = user_schema.load(request.get_json())
        except:
            return jsonify(status=400, code=104)
        try:
            user = User.query.get(user_id)
        except:
            return jsonify(status=500, code=102)
        if not data["password"]:
            return jsonify(status=400, code=105)
        if user is None:
            return jsonify(status = 404, code=103)
        
        user.password = data["password"]
        user.last_change_at = now()
        user.failed_auth_at = None
        user.failed_auth_count = 0
        user.expires_at = user_expires_at()
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)
        user_schema = UserSchema()
        return jsonify({"user": user_schema.dump(user)})
        

    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
        except:
            return jsonify(status=500, code=102)
        if user is None:
            return jsonify(status = 404, code = 103)

        db.session.delete(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500, code=102)

        return jsonify()

