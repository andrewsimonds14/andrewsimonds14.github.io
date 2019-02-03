import requests
from flask import Flask
app = Flask(__name__)

@app.route("/relaxnation/")
def home():
    return requests.get('http://andrewsimonds14.github.io').content

@app.route("/relaxnation/quiz.html/")
def quiz():
    return requests.get('http://andrewsimonds14.github.io/quiz.html').content
