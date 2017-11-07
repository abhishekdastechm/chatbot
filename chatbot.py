
from flask import Flask,jsonify,render_template,redirect, url_for, abort, session,Response,make_response,request, session, abort,flash
from flask_restful import Resource, Api
import cx_Oracle
import pandas as pd
import os
from functools import wraps
app = Flask(__name__)
api = Api(app)


######### Index Page ##########
@app.route('/home')
@login_required
def home():
    return render_template('index.html') #cust_trees.html 

########### Application Secret Key #############
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
	
app.run(host='135.66.30.14',port=5008,debug=True)	
#app.run(host='135.37.133.69',port=5008,debug=True)



