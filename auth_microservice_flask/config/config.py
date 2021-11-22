from os import environ

class Config:

    # ================== Global Configuration=====================

    ENV = environ.get("AUTHMAN_ENV", "production")

    TESTING = int(environ.get("AUTHMAN_TESTING", "0"))

    DEBUG = int(environ.get("AUTHMAN_DEBUG", "0"))


    # ================== Database Configuration=====================

    SQLALCHEMY_DATABASE_URI = environ.get("AUTHMAN_DATABASEURI", None)

    SQLALCHEMY_ECHO = DEBUG

    SQLALCHEMY_RECORF_QUERIES = DEBUG

    SQLALCHEMY_TRACK_MODIFICATION = DEBUG