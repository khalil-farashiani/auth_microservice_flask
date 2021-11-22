from flask_restful import Resource
from auth_microservice_flask.controller.apiv1 import UserController

#view(resource)
class UserResource(Resource):
    
    def get(self, user_id=None):
        """
        GET /users --> Get list of users
        GET /users/<user_id> --> Get user info
        """
        if user_id is not None:
            return UserController.get_users() # Get list of users
        else:
            return UserController.get_user(user_id) # Get user info


    def post(self):
        """
        POST /users --> Create new user
        POST /users/<user_id> --> Not allowed
        """
        return UserController.create_user() # Create new user

    def patch(self, user_id):
        """
        PATCH /users --> Not allowed
        PATCH /users/<user_id> --> Update user
        """
        return UserController.update_user(user_id) # update the user

    def delete(self, user_id):
        """
        DELETE /users --> Not allowed
        DELETE /users/<user_id> --> Delete user
        """
        return UserController.delete_user(user_id) #delete the user

