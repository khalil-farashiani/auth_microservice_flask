from auth_microservice_flask.util  import jsonify
from auth_microservice_flask.auth_microservice_flask import db
from auth_microservice_flask.model  import User
from auth_microservice_flask.schema.apiv1  import UserSchema

class UserController:
    
    def get_users():
        users_schema = UserSchema(many=True)
        users = User.query.all()

        return jsonify(
            {"users": users_schema.dump(users)}
        )

    def get_user(user_id):
        user_schema = UserSchema()
        user = User.query.get(user_id)
        if user is None:
            return jsonify(status = 404, code = 101)

    def create_user():
        return jsonify(status=500)

    def update_user(user_id):
        return jsonify(status=500)

    def delete_user(user_id):
        return jsonify(status=500)

