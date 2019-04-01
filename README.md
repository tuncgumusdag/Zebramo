# Zebramo
Zebramo Project in Python language

## Requirements

Requirement:
1. Crawl all products from this web site
https://www.influenster.com/reviews/makeup
2. Collect following properties for each product:
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
1. Implement everything on Python3 
2. Use Virtual environment and pip3 for package management
3. Use BeautifulSoup for web scraping (extracting HTML elements)
4. Use SQLAlchemy for database processing
5. Use Flask and Flask-Admin for web based admin dashboard
6. Use Flask-SQLAnchemy to integrate SQLAlchemy with Flask
7. Use Gunicorn for web-server on your local machine to serve the admin dashboard

## Description

1. Use testProject as virtual environment.
2. To run the program use run.py
3. run.py uses flaskdb package to run the program.
4. After the first run database will be created in the flaskdb package folder.
5. flaskdb/templates folder contains the htmls used for the program.
6. In flaskdb package, crawl.py used to get the product information, models is used for flask admin views and database tables, routes is used to declare informations for the pages in the flask webpage.

## Step-by-Step
1. Use testProject as virtual environment.
2. Execute run.py by either python or gunicorn.
3. Wait for program to crawl and get the information into a designated local database.
4. Enter the flask web application.
5. It will deploy itself on localhost:8000, either use localhost:8000 and click on Access Database button or use localhost:8000/admin and open Products tab to view the database.




