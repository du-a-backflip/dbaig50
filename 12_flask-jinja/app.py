# Dua Baig
# SoftDev
# Sep 2024

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
The code probably wouldn't work, as it uses a render_template command in line 
41 (and if it were to be removed from the first line, it presumably wouldn't be imported in).
Q1:
Yes, The predicted URL is http://127.0.0.1:5000/my_foist_template
Q2:
Model_tmplt.html is the file containing the html template for the website, the value of foo
is meant to be the name of the webpage (with it being between two title tags in the html file),
and the values in collections are what is being listed on the page.

DISCO:
-  Changing the value of coll changes what's listed on the page.
- {% for item in collection %}
     {{ item }} is a for loop in the html file
- using https in the url doesn't work, page not found
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask#, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
