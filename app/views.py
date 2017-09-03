
from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/contact')
def about():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('login.html')

