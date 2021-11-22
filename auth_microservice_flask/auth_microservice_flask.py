from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from auth_microservice_flask.config import Config

db = SQLAlchemy()
mg = Migrate()

apiv1_bp = Blueprint("apiv1", __name__, url_prefix='/api/v1/')
apiv1 = Api(apiv1_bp)

from auth_microservice_flask import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #load application configs 
    db.init_app(app) #initial SQLAlchemy
    mg.init_app(app, db) #initial migration
    app.register_blueprint(apiv1_bp) #load API v1 
    
    return app 
