"""
from flask import Flask 
from flask import render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

Hello = Hello

@app.route('/hello')
def hello_world():
    return 'Hello Me'
    
"""