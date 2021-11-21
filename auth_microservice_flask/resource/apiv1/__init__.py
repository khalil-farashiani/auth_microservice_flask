from auth_microservice_flask.auth_microservice_flask import apiv1 as api
from auth_microservice_flask.resource.apiv1.user import UserResource

api.add_resource(
    UserResource,
    "/users",
    methods=["GET", "POST"],
    endpoint="users",
)

api.add_resource(
    UserResource,
    "/users/<user_id>",
    methods=["GET", "PATCH", "DELETE"],
    endpoint="user"
)