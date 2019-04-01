from flask import render_template
from flaskdb import app,db
from flaskdb.models import User, Product

@app.route("/")
def start():
	return render_template('home.html')

@app.route("/database", methods=['POST'])
def database():
	cur = db.session.execute('SELECT * from product')
	products = [dict(ID=row[0], title = row[1], url = row[2],
					 star_rating = row[3], description = row[4],
					 main_image = row[5], images = row[6])
					 for row in cur.fetchall()]
	db.session.close()
	return render_template('database.html', products=products)

	