# Dua Baig
# SoftDev
# K18 - rendering an html page (with styling) using Flask
# October 16, 2024
# Time Spent:

import random
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return render_template('index.html')

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
