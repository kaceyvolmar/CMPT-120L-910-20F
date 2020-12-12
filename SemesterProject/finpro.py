import logging
from flask import Flask, render_template

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.route('/')
def index():
    app.logger.info("Switching to Index Page.")
    return render_template('index.html')


@app.route('/cody')
def cody():
    app.logger.info("Switching to Codel Page.")
    return render_template('cody.html')



@app.route('/content')
def content():
    app.logger.info("Switching to Content Page.")
    return render_template('content.html')



@app.route('/answers')
def answers():
    app.logger.info("Switching to Answers Page.")
    return render_template('answers.html')


@app.route('/404')
def four_oh_four():
    app.logger.info("Switching to 404 Page.")
    return render_template('four_oh_four.html')

@app.errorhandler(404)
def page_not_found(error):
    app.logger.warning("Switching to 404 Page.")
    return render_template('four_oh_four.html'), 404


