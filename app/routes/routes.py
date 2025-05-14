from flask import render_template, request,session
from app import app  # this imports the app object created in __init__.py
from app.game_logic import player_gen
# from app.game_logic.sqldb import reset_database
app.secret_key= "kobe"
from app.game_logic.sqldb import conn

print(app.url_map)

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

@app.route('/rosters', methods=['GET'])
def rosters():
    current_team_name= session.get('team_name',None)

    selected_team= request.args.get('team', current_team_name)

    cur=conn.cursor()

    cur.execute("SELECT DISTINCT team FROM players ORDER by team;")

    teams= [row[0] for row in cur.fetchall()]

    if not selected_team and teams:
        selected_team = teams[0]

    cur.execute("""
            SELECT name, position
              FROM players
             WHERE team = %s
          ORDER BY
            CASE WHEN position = 'G' THEN 3
                 WHEN position = 'D' THEN 2
                 ELSE 1
            END,
            name;
        """, (selected_team,))
    players = cur.fetchall()
    cur.close()

    roster = {'Forwards': [], 'Defense': [], 'Goalies': []}
    for name, position in players:
        if position == 'G':
            roster['Goalies'].append(name)
        elif position in ('LD', 'RD', 'LD/RD'):
            roster['Defense'].append(name)
        else:
            roster['Forwards'].append(name)

    return render_template(
        'roster.html',
        teams=teams,
        selected_team=selected_team,
        roster=roster
    )

