from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
from flask_pymongo import PyMongo

from flask_login import login_user, LoginManager
from restcrest.config import configDetails

app = Flask(__name__)



app.config['SECRET_KEY'] = configDetails['SECRET_KEY']
app.config["MONGO_URI"] = configDetails["MONGO_URI"] 
app.config["CURRENT_USER"] = None
app.config["CURRENT_USER_NAME"] = "Anonymous"
app.config["CURRENT_PFP"] = configDetails["CURRENT_PFP"] 
app.config["LOGO"] = configDetails["LOGO"] 
app.config["APP_NAME"] = "The Rest Crest"
# app.config.from_pyfile('config.py')


mongodb_client = PyMongo(app)
db = mongodb_client.db
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'





from restcrest import routes

