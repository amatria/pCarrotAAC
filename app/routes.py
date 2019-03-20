from flask import render_template, send_from_directory
from config import Config
from app import app, mysql

import os

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home", config=Config)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon")
