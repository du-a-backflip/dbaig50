# Dua Baig
# Team 45
# SoftDev
# October 10 2024

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import make_response

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' ) #renders login page

@app.route("/auth", methods=['POST'])
def authenticate():
    user = request.form['username']
    resp = make_response(render_template( 'response.html' , foo = request.form['username'])) #allows for greater customization than just flask.Response()
    resp.set_cookie('userID', user)
    return resp #renders

@app.route("/logout", methods=['GET'])
def logout():
    name = request.cookies.get('userID')
    return render_template( 'logout.html' , foo = name)
    
if __name__ == "__main__": #false if this file imported as module
    app.debug = True 
    app.run()