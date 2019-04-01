from flaskdb import db, admin
from flask_admin.contrib.sqla import ModelView

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	password = db.Column(db.String(30), nullable=False)

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))
	url = db.Column(db.String(50))
	description = db.Column(db.String(500))
	star_rating = db.Column(db.String(5))
	main_image = db.Column(db.String(50), default='default.jpg')
	images = db.Column(db.String(200), default='default.jpg')


#admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Product, db.session))