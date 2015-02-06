import os
import os.path as op

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext import restful

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib import fileadmin

from flask.ext.bcrypt import Bcrypt
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

api = restful.Api(app)

# flask-bcrypt
flask_bcrypt = Bcrypt(app)

# flask-httpauth
auth = HTTPBasicAuth()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

from app import views
from app.models import User,Post

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))

admin.add_view(fileadmin.FileAdmin(app.config['FILE_PATH'], '/files/', name='Files'))