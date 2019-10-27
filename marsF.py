import scrape_mars 
from flask import Flask, render_template, url_for,jsonify,request,redirect
from flask_pymongo import PyMongo
from splinter import Browser


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_info"
mongo = PyMongo(app)


@app.route("/")
def home():
    scrape_dict = mongo.db.scrape_dict.find_one()
    
    return render_template("marsV.html", mars=scrape_dict)
    

@app.route("/scrape")
def scraper():
    scrape_dict = mongo.db.scrape_dict
    scrape_data=scrape_mars.scraping()
    scrape_dict.update({}, scrape_data, upsert=True)
    return redirect("/", code=302)

if __name__=='__main__':
    app.run(debug=True)
