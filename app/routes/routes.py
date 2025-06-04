from calendar import firstweekday

from flask import render_template, request,session
from app import app  # this imports the app object created in __init__.py
from app.game_logic import player_gen
app.secret_key= "kobe"
from app.game_logic.sqldb import conn
from app.game_logic.player_value import playerValue
from flask import render_template, request, session, flash, redirect, url_for
from app.game_logic import player_value
from app.game_logic.sqldb import fetch_all_team_names, fetch_team_roster
from app.game_logic.game_engine import GameEngine

import calendar
from datetime import date

engine= GameEngine()

def ensure_players_exist():
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM players;")
    count = cur.fetchone()[0]
    if count == 0:
        generator = player_gen.player_generation()
        generator.create_players()
    cur.close()
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
    ensure_players_exist()
    engine.start_season()

    year= int(request.args.get('year',2025))
    month = int(request.args.get('month', 10))

    first_weekday_mon, days_in_month = calendar.monthrange(year, month)
    first_weekday_sun = (first_weekday_mon + 1) % 7

    team = session.get('team_name')
    games_by_day = {}

    for game_date, home, away in engine.schedule:
        if game_date.year == year and game_date.month == month:
            if home == team or away == team:
                d = game_date.day
                matchup = f"{home} vs {away}"
                games_by_day.setdefault(d, []).append(matchup)

    return render_template(
        'game.html',
        team=team_name,
        current_month=month,
        current_year=year,
        first_weekday_sun=first_weekday_sun,
        days_in_month=days_in_month,
        games_by_day=games_by_day
    )

@app.route('/home-screen-managing-hockey-gm', methods=['GET'])
def sidebar_home():
    # 1) If no team has been chosen, send them to the “newGame” page.
    if 'team_name' not in session:
        return redirect(url_for('newGame'))

    team_name = session['team_name']

    # 2) Ensure schedule exists. If not, kick off a new season.
    if not hasattr(engine, 'schedule'):
        engine.start_season()

    #  Read month/year from query params if provided; otherwise default to October 2025
    month = int(request.args.get('month', 10))
    year  = int(request.args.get('year', 2025))

    first_weekday_mon, days_in_month = calendar.monthrange(year, month)
    first_weekday_sun = (first_weekday_mon + 1) % 7

    games_by_day = {}
    for game_date, home, away in engine.schedule:
        if game_date.year == year and game_date.month == month:
            # Only include days involving our team
            if home == team_name or away == team_name:
                d = game_date.day
                matchup = f"{home} vs {away}"
                games_by_day.setdefault(d, []).append(matchup)

    return render_template(
        'game.html',
        team=team_name,
        current_month=month,
        current_year=year,
        first_weekday_sun=first_weekday_sun,
        days_in_month=days_in_month,
        games_by_day=games_by_day
    )

@app.route('/rosters', methods=['GET'])
def rosters():
    current = session.get('team_name')
    teams = fetch_all_team_names()
    selected_team = request.args.get('team', current or (teams[0] if teams else None))

    # YOUR single source of truth for the roster
    players = fetch_team_roster(selected_team)
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
        'Name','Potential', 'Position', 'Age', 'Height', 'Weight', 'Shooting', 'Determination', 'Passing',
        'Vision', 'Defense', 'Skating', 'Speed', 'Overall'
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

@app.route('/trades', methods=['GET', 'POST'])
def trades():
    current_team  = session.get('team_name', 'Your Team')
    selected_team = request.args.get('team', current_team)

    # ─── get all team names in one call ───
    teams = fetch_all_team_names()
    if not selected_team and teams:
        selected_team = teams[0]

    # ─── use the same roster helper for BOTH sides ───
    players       = fetch_team_roster(current_team)
    other_players = fetch_team_roster(selected_team)

    # ─── compute values just like before ───
    col_indices = {
        'name': 0, 'potential': 1, 'age': 2,
        'weight': 3, 'height': 4, 'position': 5,
        'overall_rating': 6
    }

    player_values = []
    for player in players:
        name            = player[col_indices['name']]
        position        = player[col_indices['position']]
        potential       = player[col_indices['potential']]
        age             = player[col_indices['age']]
        overall_rating  = player[col_indices['overall_rating']]

        value = playerValue(name, position, potential, age, overall_rating)
        player_values.append((name, value.calculate_value()))

    other_player_values = []
    for player in other_players:
        name   = player[col_indices['name']]
        pos    = player[col_indices['position']]
        pot    = player[col_indices['potential']]
        age    = player[col_indices['age']]
        rating = player[col_indices['overall_rating']]

        val = playerValue(name, pos, pot, age, rating)
        other_player_values.append((name, val.calculate_value()))

    columns = [
        'Name', 'Potential', 'Age',
        'Weight', 'Height', 'Position',
        'Overall Rating', 'Player Value'
    ]

    return render_template(
        'trades.html',
        teams=teams,
        current_team=current_team,
        selected_team=selected_team,
        players=players,
        other_players=other_players,
        columns=columns,
        col_indices=col_indices,
        player_values=player_values,
        other_player_values=other_player_values
    )

@app.route('/propose_trade', methods=['POST'])
def propose_trade():
    current_team  = session.get('team_name', 'Your Team')
    selected_team = request.form.get('team', current_team)

    team1_names = request.form.getlist('team1_players')
    team2_names = request.form.getlist('team2_players')

    cur = conn.cursor()

    def fetch_valobj(name):
        cur.execute(
            "SELECT name, position, potential, age, overall_rating "
            "FROM players WHERE name = %s",
            (name,)
        )
        row = cur.fetchone()
        return playerValue(*row) if row else None

    team1_objs = [o for n in team1_names if (o := fetch_valobj(n))]
    team2_objs = [o for n in team2_names if (o := fetch_valobj(n))]

    # check fairness
    fair = playerValue.isTradeFair(team1_objs, team2_objs)

    if fair:
        #move team1 players to selected_team
        for name in team1_names:
            cur.execute(
                "UPDATE players SET team = %s WHERE name = %s",
                (selected_team, name)
            )

        #move team2 players to current_team
        for name in team2_names:
            cur.execute(
                "UPDATE players SET team = %s WHERE name = %s",
                (current_team, name)
            )

        # commit once
        conn.commit()
        flash("Trade completed successfully! ✅")

    else:
        flash("Trade is NOT fair — no changes applied. ❌")

    cur.close()
    return redirect(url_for('trades', team=selected_team))

