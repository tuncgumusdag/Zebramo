from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///flaskdb/host.db')
Base = declarative_base()

print('[CRAWL-INFO] : Starting crawling operations...')

class Product(Base):
	__tablename__ = 'product'

	id = Column(Integer, primary_key=True)
	title = Column(String(50))
	url = Column(String(200))
	star_rating = Column(String(5))
	description = Column(String(500))
	main_image = Column(String(200), default='default.jpg')
	images = Column(String(50), default='default.jpg')

Session = sessionmaker(bind=engine) 
Base.metadata.create_all(bind=engine)

site= 'https://www.influenster.com/reviews/makeup'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

products = soup.findAll(class_='category-product')

print('[CRAWL-INFO] : Starting crawling through ' + site)

session = Session()

for product in products:

	title = product.find(class_='category-product-title')
	title = title.text

	check_db_for_item = session.query(Product.id).filter(Product.title==title)

	if session.query(check_db_for_item.exists()).scalar() == True:
		print('[CRAWL-INFO] : \"' + title + '\" already exists in the database, skipping...')
		continue

	product_link = 'https://www.influenster.com' + product.get('href')

	rating = product.find(class_='category-product-rating')
	rating = rating.strong.text

	site = product_link
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = Request(site,headers=hdr)
	page = urlopen(req)
	soup = BeautifulSoup(page, 'html.parser')

	desc = soup.find(class_="product-description")
	desc = desc.p.text

	images = soup.findAll('li', class_='product-image-link', limit=10)
	if 	len(images) is 0:
		image = soup.find(class_='product-image')
		img_list = image.img['src']
		main_img = img_list
	else:
		img_list=''
		for image in images:
			img_list += image.find('input')['data-image-url'] + ' '
		main_img = images[0].find('input')['data-image-url']
	
	product_to_add = Product(title=title, url=product_link, star_rating=rating, description=desc, main_image=main_img, images=img_list)

	session.add(product_to_add)
	session.commit()

	print('[CRAWL-INFO] : \"' + title + '\" has been successfully committed to database.')

print('[CRAWL-INFO] : All operations are done.')


