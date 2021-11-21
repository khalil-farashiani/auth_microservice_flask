from flask_restful import Resource

class UserResource(Resource):

    def get(self, user_id=None):
        if user_id is not None:
            return {"user":"singlton"}

        return {"user": "collection"} 

