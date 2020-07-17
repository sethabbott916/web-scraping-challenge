from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_yo


app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_scrape_data")


@app.route('/')
def index():
    mars = mongo.db.mars.find_one()

    print(mars)

    return render_template('index.html', mars=mars)


@app.route('/scrape')
def scrape():
    
    mars_scrape_data = mars_yo.scrape_info()

    print("*******Loook Here****************")
    print(mars_scrape_data)
    
    mongo.db.mars.update({}, mars_scrape_data, upsert=True)

    
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
