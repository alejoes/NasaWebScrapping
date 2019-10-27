from scrape_mars import scraping
from flask import Flask, render_template, url_for,jsonify,request

app = Flask(__name__)



@app.route("/scrape")



@app.route("/api/v1.0/precipitation")
def scrape():



if __name__=='__main__':
    app.run(debug=True)
