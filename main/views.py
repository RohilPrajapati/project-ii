from main import app
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from main.algorithms import bisection,newton_raphson,false_position,fixed_point
from main.init_db import get_db_connection
from main.db_helper import create_user,fetch_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html',response={'data_status':False})
    if request.method == 'POST':
        print(request)
        eqn = request.form['eqn']
        a = request.form['a']
        b = request.form['b']
        algo = request.form['algo']
        response = {}
        if algo == "bisection":
            response = bisection(eqn,a,b)
            response['result_status']= True
        elif algo == "newtonRaphson":
            response = newton_raphson(eqn,a)
        elif algo == "falsePosition":
            response = false_position(eqn,a,b)
        elif algo == "fixedPoint":
            response = fixed_point(eqn,a,b)
        return render_template('index.html',response=response)
    
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if session['id']:
            return redirect(url_for('index'))
        return render_template('pages/login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # print(username,password)
        user = fetch_user(username)
        if not user:
            response = {
                'message':'Username is not register'
            }
            return render_template('pages/login.html',response=response)
        if not check_password_hash(user['password'],password):
            response = {
                'message':'Password Incorrrect'
            }
            return render_template('pages/login.html',response=response)
        session['id']= user['id']
        session["username"] = user['username']
        response = {
            'message':'Login Success'
        }
        return redirect(url_for('index'))
        # return render_template('pages/login.html',response=response)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('pages/register.html')
    elif request.method == 'POST':
        print(request)
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        h_pass = generate_password_hash(password)
        print(h_pass)
        create_user(username=username,email=email,password=h_pass)
        return render_template('pages/register.html')

@app.route('/logout',methods=['GET'])
def logout():
    if request.method == 'GET':
        session['id']= None
        session["username"] = None
        response = {
            'message':'User have been logout'
        }
        return render_template('pages/login.html',response = response)
