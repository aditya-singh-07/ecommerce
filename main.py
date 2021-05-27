from flask import Flask, Blueprint, render_template

app = Flask(__name__)

main = Blueprint('main', __name__)
@main.route('/shopping')
def shopping():
    return render_template('index.html')

@main.route('/food')
def court():
    return render_template('index.html')

@main.route('/movie')
def movie():
    return render_template('index.html')