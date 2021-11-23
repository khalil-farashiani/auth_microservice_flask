from datetime import datetime, timedelta

from auth_microservice_flask.config import Config
from auth_microservice_flask.util import now

def user_expires_at():
    return now() + timedelta(days=Config.USER_DEFUALT_EXPIRES)