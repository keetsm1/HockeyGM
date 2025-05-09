import psycopg2

conn= psycopg2.connect(
        dbname="hockeygm",
        user="postgres",
        password="Ramanjit12!",
        host="localhost",
        port= "5432"
    )

cur= conn.cursor()

def save_to_database(player):
    query = """
    INSERT INTO players (
        name, potential, age, weight, height, position,
        shooting, determination, passing, vision,
        dman_defense, forward_defense, skating, speed,
        rebound_control, technique, glove, blocker, 
        puck_handling, composure
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        player.name, player.potential, player.age, player.weight,
        player.height, player.position, player.shooting, player.determination,
        player.passing, player.vision, player.dman_defense, player.forward_defense,
        player.skating, player.speed, player.rebound_control, player.technique,
        player.glove, player.blocker, player.puck_handling, player.composure
    )
    cur.execute(query, values)
    conn.commit()

# cur.close()
# conn.close()