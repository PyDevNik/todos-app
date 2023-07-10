import os, sys
sys.path.append("..")

from flask import Flask
from flask_login import LoginManager
from db.db import DB

app = Flask(__name__)
app.secret_key = "ValikMoyDrug"
app.template_folder = os.path.abspath("../../frontend/html")
app.static_folder = os.path.abspath("../../frontend/css")

db = DB()

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return db.get_user(id=user_id)
login_manager.login_view = "login"

def generate_id():
    return db.generate_id()

from routes.auth import *
from routes.todos import *