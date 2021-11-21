from os import environ

class Config:

    # ================== Global Configuration=====================
    ENV = environ.get("AUTHMAN_ENV", "production")

    TESTING = int(environ.get("AUTHMAN_TESTING", "0"))

    DEBUG = int(environ.get("AUTHMAN_DEBUG", "0"))