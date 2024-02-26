import os
from os import path
from flask import Flask, render_template, request, Response, redirect, url_for
from flask_pymongo import PyMongo


if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "Planner"
app.config["MONGO_URI"]="mongodb+srv://root:Dunedin100@myfirstcluster.jekwe.mongodb.net/planner?retryWrites=true&w=majority"


mongo = PyMongo(app) 







@app.route("/")
def index():
    
    
    
    return render_template("index.html", x=mongo.db.Test1.find())








if __name__ == "__main__":
    app.run(debug=True)
