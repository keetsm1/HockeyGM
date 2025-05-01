from flask import render_template, request
from app import app  # this imports the app object created in __init__.py

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/newGame')
def newGame():
    return render_template('newGame.html')

@app.route('/startGame', methods= ['POST'])
def startGame():
    team_name= request.form['team']
    return render_template('game.html', team= team_name);