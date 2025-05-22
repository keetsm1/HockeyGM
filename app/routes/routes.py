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
            SELECT name, potential,age,weight,height, position, shooting, determination,passing,vision,dman_defense,forward_defense,skating,
                   speed, rebound_control, technique,glove,blocker,puck_handling, composure,overall_rating
            FROM players
            WHERE team= %s
            ORDER BY position,name;
        """, (selected_team,))
    players = cur.fetchall()
    cur.close()
    col_indices = {
        'name': 0, 'potential': 1, 'age': 2, 'weight': 3, 'height': 4, 'position': 5,
        'shooting': 6, 'determination': 7, 'passing': 8, 'vision': 9, 'dman_defense': 10,
        'forward_defense': 11, 'skating': 12, 'speed': 13, 'rebound_control': 14,
        'technique': 15, 'glove': 16, 'blocker': 17, 'puck_handling': 18, 'composure': 19,
        'overall_rating': 20
    }

    forwards= []
    defensemen = []
    goalies = []

    for player in players:
        position = player[5]  # position is the 6th element (0-indexed)
        if position == 'G':
            goalie_data = (
                player[col_indices['name']],
                player[col_indices['potential']],
                player[col_indices['age']],
                player[col_indices['weight']],
                player[col_indices['height']],
                player[col_indices['position']],
                player[col_indices['glove']],
                player[col_indices['blocker']],
                player[col_indices['rebound_control']],
                player[col_indices['composure']],
                player[col_indices['overall_rating']]
            )
            goalies.append(goalie_data)
        elif 'D' in position.upper():
            defenseman_data = (
                player[col_indices['name']],
                player[col_indices['potential']],
                player[col_indices['position']],
                player[col_indices['age']],
                player[col_indices['height']],
                player[col_indices['weight']],
                player[col_indices['shooting']],
                player[col_indices['determination']],
                player[col_indices['passing']],
                player[col_indices['vision']],
                player[col_indices['dman_defense']],  # Using the defensive stat for defensemen
                player[col_indices['skating']],
                player[col_indices['speed']],
                player[col_indices['overall_rating']]
            )
            defensemen.append(defenseman_data)
        else:
            forward_data = (
                player[col_indices['name']],
                player[col_indices['potential']],
                player[col_indices['age']],
                player[col_indices['weight']],
                player[col_indices['height']],
                player[col_indices['position']],
                player[col_indices['shooting']],
                player[col_indices['determination']],
                player[col_indices['passing']],
                player[col_indices['vision']],
                player[col_indices['forward_defense']],  # Using forward_defense for forwards
                player[col_indices['skating']],
                player[col_indices['speed']],
                player[col_indices['overall_rating']]
            )
            forwards.append(forward_data)

    forwards_columns= [
        'Name', 'Potential', 'Age', 'Weight', 'Height', 'Position', 'Shooting',
        'Determination', 'Passing', 'Vision', 'Forward Defense', 'Skating',
        'Speed', 'Overall'
    ]
    defensemen_columns = [
        'Name', 'Position', 'Age', 'Height', 'Weight', 'Shooting', 'Determination', 'Passing',
        'Vision', 'Forward Defense', 'Skating', 'Speed', 'Overall'
    ]
    goalies_columns = [
        'Name', 'Potential', 'Age', 'Weight', 'Height', 'Position', 'Glove',
        'Blocker', 'Rebound Control', 'Composure', 'Overall'
    ]

    return render_template(
        'roster.html',
        teams=teams,
        selected_team=selected_team,
        players= players,
        forwards = forwards,
        defensemen=defensemen,
        goalies=goalies,
        forwards_columns=forwards_columns,
        defensemen_columns=defensemen_columns,
        goalies_columns=goalies_columns
    )

@app.route('/trades', methods=['GET'])
def trades():
    return render_template('trades.html')
