from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # # Find one record of data from the mongo database
    #data={} 
    destination_data=mongo.db.collection.find_one()


    # # Return template and data
    return render_template("index.html", data=destination_data)
    


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    data = scrape_mars.scrape()
    mongo.db.collection.insert(data)
    # use mongo update to upsert data
    mongo.db.collection.update({},data, upsert=True)
    
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
