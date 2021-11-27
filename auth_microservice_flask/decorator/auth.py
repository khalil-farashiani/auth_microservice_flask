from functools import wraps
from flask import request, g
from jwt import decode
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError

from auth_microservice_flask.config import Config
from auth_microservice_flask.model import User
from auth_microservice_flask.util import jsonify, now
from auth_microservice_flask.rule import ControllerAccessRules

def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "X-Disable-AuthRequired" in request.headers:
            if Config.TESTING and request.headers["X-Disable-AuthRequired"] == "YES":
                return f(*args, **kwargs)
        controller_authorized_roles = ControllerAccessRules.get_controller_rules(f.__name__)
        if controller_authorized_roles is False:
            return jsonify(status=500, code=115)
        if controller_authorized_roles is None:
            g.anonymous = True
            g.privileged = False
            return f(*args, **kwargs)
        if "X-Auth-Token" not in request.headers:
            return jsonify(status=401, code=112)
        try:
            data = decode(
                request.headers.get("X-Auth-Token"),
                Config.SECRET_KEY,
                algorithms=[Config.USER_DEFAULT_TOKEN_ALGO]
            )
        except InvalidSignatureError:
            return jsonify(status=401, code=113)
        except ExpiredSignatureError:
            return jsonify(status=401, code=121)
        except:
            return jsonify(status=401, code=114)
        try:
            user = User.query.get(data["user"]["id"])
        except:
            return jsonify(status=500, code=102)
        if user is None:
            return jsonify(status=401, code=103)
        if user.role != data["user"]["role"]:
            return jsonify(status=401, code=111)
        if user.expires_at < now():
            return jsonify(status=401, code=108)
        if user.status != 3:
            if user.status == 0:
                return jsonify(status=401, code=118)
            if user.status == 1:
                return jsonify(status=401, code=119)
            if user.status == 2:
                return jsonify(status=401, code=120)
        if user.role in controller_authorized_roles:
            g.anonymous = False
            g.privileged = True
        elif "member:user_id" in controller_authorized_roles:
            g.anonymous = False
            g.privileged = False
            if user.id != args[f.__code__.co_varnames.index("user_id")]:
                return jsonify(status=403, code=116)
        else:
            return jsonify(status=401, code=117)
        return f(*args, **kwargs)
    return wrapper
