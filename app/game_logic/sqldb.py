import psycopg2
from psycopg2.extras import RealDictCursor

conn= psycopg2.connect(
    dbname="hockeygm",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
    )
conn.autocommit = True
cur= conn.cursor()

def save_to_database(player):
    query = """
    INSERT INTO players (
        name, potential, age, weight, height, position,
        shooting, determination, passing, vision,
        dman_defense, forward_defense, skating, speed,
        rebound_control, technique, glove, blocker, 
        puck_handling, composure, team, overall_rating, salary
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        player.name, player.potential, player.age, player.weight,
        player.height, player.position, player.shooting, player.determination,
        player.passing, player.vision, player.dman_defense, player.forward_defense,
        player.skating, player.speed, player.rebound_control, player.technique,
        player.glove, player.blocker, player.puck_handling, player.composure, player.team, player.overall_rating,
        player.salary
    )
    cur.execute(query, values)
    conn.commit()

# cur.close()
# conn.close()
def fetch_player_tallies(team_name:str):
    cur= conn.cursor()
    cur.execute("""
        SELECT player_name, G, A, Points 
        FROM player_tallies
        WHERE team_name = %s
        ORDER BY Points DESC, G DESC;
    """,(team_name,))
    rows= cur.fetchall()
    cur.close()
    return rows

def fetch_rankings():
    cur=conn.cursor()
    cur.execute("""
        SELECT team_name, W, L, OTL, Points
        FROM rankings
        ORDER BY Points DESC, W DESC;
    """)
    rows= cur.fetchall()
    cur.close()
    return rows

def save_player_stats(player_name: str, team_name: str, goals: int, assists: int, points: int):
    with conn.cursor() as cur:
        query = """
        INSERT INTO player_tallies (
            player_name,
            team_name,
            G,
            A,
            Points
        ) VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (player_name)
        DO UPDATE
          SET
            G      = player_tallies.G + EXCLUDED.G,
            A      = player_tallies.A + EXCLUDED.A,
            Points = player_tallies.Points + EXCLUDED.Points,
            team_name = EXCLUDED.team_name;
        """
        values = (player_name, team_name, goals, assists, points)
        cur.execute(query, values)
        conn.commit()

def save_team_stats(team_name: str, W: int, L: int, OTL:int,points: int):
    with conn.cursor() as cur:
        query = """
        INSERT INTO rankings (
            team_name,
            W,
            L,
            OTL,
            Points
        ) VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (team_name)
        DO UPDATE
          SET
            W      = EXCLUDED.W,
            L      = EXCLUDED.L,
            OTL    = EXCLUDED.OTL,
            Points = EXCLUDED.Points;
        """
        values = (team_name, W, L,OTL, points)
        cur.execute(query, values)
        conn.commit()

def fetch_team_roster(team):
    """
    """
    cur = conn.cursor()
    cur.execute("""
        SELECT name, potential, age, weight, height, position, overall_rating, salary
        FROM players
        WHERE team = %s
        ORDER BY position, name;
    """, (team,))
    rows = cur.fetchall()
    cur.close()
    return rows

def fetch_all_team_names():
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT team FROM players ORDER BY team;")
    teams = [row[0] for row in cur.fetchall()]
    cur.close()
    return teams


def fetch_team_roster_full(team: str):
    """
    Return a list of dicts, each dict containing all the columns
    that simulate_game() and calculate_ratings() expect.
    This does NOT replace fetch_team_roster(); it’s a separate function.
    """
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT
            name                AS "Name",
            potential           AS "Potential",
            age                 AS "Age",
            weight              AS "Weight",
            height              AS "Height",
            position            AS "Position",
            shooting            AS "Shooting",
            determination       AS "Determination",
            passing             AS "Passing",
            vision              AS "Vision",
            dman_defense        AS "Dman Defense",
            forward_defense     AS "Forward Defense",
            skating             AS "Skating",
            speed               AS "Speed",
            rebound_control     AS "Rebound Control",
            technique           AS "Technique",
            glove               AS "Glove",
            blocker             AS "Blocker",
            puck_handling       AS "Puck Handling",
            composure           AS "Composure",
            team                AS "Team",
            overall_rating      AS "Overall"
        FROM players
        WHERE team = %s
        ORDER BY position, name;
    """, (team,))
    rows = cur.fetchall()
    cur.close()
    return rows


