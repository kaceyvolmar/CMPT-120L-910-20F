from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
<<<<<<< HEAD
    return 'Hello me'

    
=======
    return render_template("index.html")
>>>>>>> parent of da7a967... Lab 6, Assignment 7
