# Zebramo
Zebramo Project in Python language

## Requirements

Requirement:
1. Crawl all products from this web site
https://www.influenster.com/reviews/makeup
2. Collect following properties for each product
Product URL
Product title
Description
Product images, max. 10 images
Decide and set which image is the main image
Star rating (from 0 to 5)
Total number of stars
3. Save each product in a database on your local machine (Sqlite)
4. Build a web based admin dashboard to be able to see all those products crawled
5. Push your code on Github and share it with us


Environment and packages:
Implement everything on Python3 
Use Virtual environment and pip3 for package management
Use BeautifulSoup for web scraping (extracting HTML elements)
Use SQLAlchemy for database processing
Use Flask and Flask-Admin for web based admin dashboard
Use Flask-SQLAnchemy to integrate SQLAlchemy with Flask
Use Gunicorn for web-server on your local machine to serve the admin dashboard
