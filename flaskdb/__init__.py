from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///host.db'
app.config['SECRET_KEY'] = 'secretkey000'
db = SQLAlchemy(app)
admin = Admin(app, name='Admin', template_mode='bootstrap3')

from flaskdb import routes
from flaskdb.models import User
