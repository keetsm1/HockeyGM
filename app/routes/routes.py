from flask import render_template
from app import app  # this imports the app object created in __init__.py

@app.route('/')
def home():
    return render_template('home.html')