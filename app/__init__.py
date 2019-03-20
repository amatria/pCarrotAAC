from flaskext.mysql import MySQL
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL()
mysql.init_app(app)

from app import routes
