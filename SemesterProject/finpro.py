import logging
from flask import Flask 
from flask import render_template


app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.route('/')
def index():
    app.logger.info("This page isn't finished yet.")
    return render_template('index.html')


