import os

class Config(object):
    # Server Info
    NAME = "pCarrotAAC"

    # Database
    MYSQL_DATABASE_USER = "inaki"
    MYSQL_DATABASE_PASSWORD = "password"
    MYSQL_DATABASE_DB = "server"
    MYSQL_DATABASE_HOST = "127.0.0.1"
    MYSQL_DATABASE_PORT = 3306

    # Extra
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supper_secret_key'
