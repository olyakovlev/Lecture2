from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, world! Using variables!! In debug mode!!!"
    return render_template("index.html", headline = headline)

@app.route("/bye")
def bye():
    headline = "Goodbye, World!!!"
    return render_template("index.html", headline = headline)
