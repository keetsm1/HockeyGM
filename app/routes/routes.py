from flask import render_template, request
from app import app  # this imports the app object created in __init__.py
from app.game_logic import player_gen


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/newGame')
def newGame():
    return render_template('newGame.html')

@app.route('/start-Game', methods= ['POST'])
def startGame():
    team_name= request.form['team']

    player = player_gen.player_generation()
    player.create_players()
    return render_template('game.html', team= team_name)
