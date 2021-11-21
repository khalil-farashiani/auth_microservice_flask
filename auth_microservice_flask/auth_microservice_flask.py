from flask import Flask, Blueprint
from auth_microservice_flask.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app 
