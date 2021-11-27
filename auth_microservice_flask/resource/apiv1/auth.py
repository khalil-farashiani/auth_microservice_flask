from flask_restful import Resource

from authman.controller.apiv1 import AuthController

class AuthResource(Resource):

    def get(self):
        """
        GET /auth/tokens --> Verify token.
        """
        return AuthController.verify_jwt_token() # Verify token.

    def post(self):
        """
        POST /auth/tokens --> Create new token.
        """
        return AuthController.create_jwt_token() # Create new token.
