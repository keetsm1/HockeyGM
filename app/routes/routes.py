from flask import render_template, request,session
from app import app  # this imports the app object created in __init__.py
from app.game_logic import player_gen
# from app.game_logic.sqldb import reset_database
app.secret_key= "???" #removed for security purposes.


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/newGame')
def newGame():
    return render_template('newGame.html')

@app.route('/start-Game', methods= ['POST'])
def startGame():
    team_name= request.form['team']
    session['team_name']= team_name
    player = player_gen.player_generation()
    player.create_players()
    return render_template('game.html', team= team_name)

@app.route('/home-screen-managing-hockey-gm', methods= ['GET'])
def sidebar_home():
    team_name= session.get('team_name','Default Team')
    return render_template('game.html', team=team_name)

@app.route('/rosters')
def rosters():
    return render_template('roster.html')
