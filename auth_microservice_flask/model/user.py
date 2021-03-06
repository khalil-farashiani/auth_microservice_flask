from auth_microservice_flask.auth_microservice_flask import db
from auth_microservice_flask.util  import uuidgen, user_expires_at, now
from auth_microservice_flask.config import Config



class User(db.Model):

    id                = db.Column(db.String(64), primary_key=True, default=uuidgen)
    username          = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password          = db.Column(db.String(256), nullable=False)
    role              = db.Column(db.String(32), nullable=False, default=Config.USER_DEFUALT_ROLE)
    created_at        = db.Column(db.DateTime, nullable=False, default=now )
    expires_at        = db.Column(db.DateTime, nullable=False, default=user_expires_at)
    last_login_at     = db.Column(db.DateTime)
    last_active_at    = db.Column(db.DateTime)
    last_change_at    = db.Column(db.DateTime)
    failed_auth_at    = db.Column(db.DateTime)
    failed_auth_count = db.Column(db.Integer, default=0)
    status            = db.Column(db.Integer, nullable=False, default=Config.USER_DEFUALT_STATUS)