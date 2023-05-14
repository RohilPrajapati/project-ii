from main import app
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from main.algorithms import bisection
# def bisection():
#         if (func(a) >= 0 and func(b) < 0 ):
#             pass
#         elif (func(b) >= 0 and func(a) <0):
#             print(func(a))
#             print(func(b))
#             a,b=b,a
#         else:
#             print("You have not assumed right a and b\n")

# response = {}
#         def func(x):
#             return x*x - 2
# 1,2


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html',response={'data_status':False})
    if request.method == 'POST':
        print(request)
        eqn = request.form['eqn']
        a = request.form['a']
        b = request.form['b']
        print(eqn)
        print(a)
        print(b)
        
        response = bisection(eqn,a,b)
        print(response)
        
        return render_template('index.html',response=response)