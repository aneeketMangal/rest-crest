from restcrest import app
from datetime import datetime
import json
from bson import json_util
from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
from flask_classful import FlaskView, route
from restcrest.database.user_database import UserDatabase
from restcrest.database.post_database import PostDatabase
from restcrest.backend.fetch_posts import FetchPost
from restcrest.forms.login_form import LoginForm
from restcrest.forms.register_form import RegisterForm
from restcrest.elements.user.user import User
from flask_login import login_user, LoginManager, current_user, login_required, logout_user
from restcrest import login_manager
from bson.objectid import ObjectId
user_db = UserDatabase()
post_db = PostDatabase()
postFetch = FetchPost()


@app.route('/')
@app.route('/home')
def home():
    posts = postFetch.getGlobalPosts()
    userData = {}
    if(app.config['CURRENT_USER']):
        userData = app.config['CURRENT_USER'].getInfo()
    return render_template('index.html', posts = posts, userData = userData)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if(current_user.is_authenticated):
        return redirect(url_for('home'))
    form = RegisterForm()
    if(form.validate_on_submit()):
        databaseLog = user_db.checkUserAvailability(form.username.data, form.email.data)
        if(databaseLog['isAvailable']):
            user_db.addUser(form.username.data, form.password.data)
            flash(f'Account created successfully {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(databaseLog['errorLog'], 'danger')

    return render_template('register.html', title = 'Register', form = form)



    
@app.route('/create', methods = ['GET', 'POST'])
def create():
    if(request.method == 'GET'):
        return render_template('create.html')
    elif(request.method == 'POST'):
        if(app.config['CURRENT_USER']):
            text = request.form['name']
            userId = app.config['CURRENT_USER'].getId()

            now = datetime.now()
            post_db.addPost(userId, text, now)
            flash('Note successfully added', 'success')
        else:
            flash('You need to be signed in to post.', 'danger')
        return redirect(url_for('home'))



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/login',  methods = ['GET', 'POST'])
def login():
   
    form = LoginForm()
    if(form.validate_on_submit()):
        databaseLog = user_db.verifyUserDetails(form.username.data,form.password.data)
        if(databaseLog['isAvailable']):
            login_user(User(databaseLog['userData']), remember = form.remember.data)
            flash(f'Welcome {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(databaseLog['errorLog'], 'danger')

    return render_template('login.html', title = 'Login', form = form)

@app.route("/test")
def addUser():
    print(current_user)
    # a = postFetch.getGlobalPosts()
    return {'success':current_user.getInfo()}


@login_manager.user_loader
def load_user(userid):
    userid = userid['$oid']
    user = user_db.getById(ObjectId(userid))
    print(user)
    if user is not None:
        print(user)
        return User(user)
    else:
        return None