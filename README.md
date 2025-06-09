HockeyGM

A web-based Hockey General Manager simulation game built with Python and Flask, featuring automatic player generation, full season scheduling, game simulation, and roster management using PostgreSQL.

Features

Player Generation: Randomly generates forwards, defensemen, and goalies with realistic attributes and ratings. 

Database Management: Stores player data in PostgreSQL using psycopg2. 

Roster Display: View team rosters sorted by position and rating. fileciteturn0file0

Game Simulation: Simulate full games including regulation and overtime, record goals, assists, and update standings.

Season Schedule: Generates a round-robin schedule plus extra matches to complete an 82-game season.

Trade Logic: Evaluate fair trades based on player value calculations.

Tech Stack

Python 3.x

Flask

Jinja2 templates

psycopg2

PostgreSQL

HTML/CSS (Google Fonts, Montserrat)

Installation

Prerequisites

Python 3.8 or higher

PostgreSQL 12 or higher

Setup

Clone the repository:

git clone https://github.com/keetsm1/HockeyGM.git
cd HockeyGM

Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt

Configure the database:

Create a PostgreSQL database named hockeygm.

Update app/game_logic/sqldb.py with your database credentials.

Generate players:

python -c "from app.game_logic.player_gen import player_generation; player_generation().create_players()"

Run the Flask app:

export FLASK_APP=app
export FLASK_ENV=development
flask run

Project Structure

HockeyGM/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── game_logic/
│   │   ├── sqldb.py
│   │   ├── player_gen.py
│   │   ├── player_value.py
│   │   └── game_engine.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── newGame.html
│   │   ├── game.html
│   │   └── ... (rosters, trades, calendar)
│   └── static/
│       ├── css/
│       └── logos/
├── requirements.txt
└── README.md

Usage

**Home: Start a new game or load an existing one:**

![image](https://github.com/user-attachments/assets/577613ef-e02a-4461-a7ba-e4c372683da5)

****Team Selection: Choose your GM team: ****

![image](https://github.com/user-attachments/assets/e2e56a48-34d2-42a3-bbd2-9264bc31646c)

**Game Dashboard: View schedules, simulate games day by day, advance calendar, Track wins, losses, overtime losses, and points:**

![image](https://github.com/user-attachments/assets/b22c8318-0b96-47e3-8731-806cc99bb55f)
![image](https://github.com/user-attachments/assets/9cf7f079-672a-4127-bf19-8ea5adb3460f)
![image](https://github.com/user-attachments/assets/16471205-2368-417f-9ab6-89236693ae9d)


**Rosters & Trades: Manage players, propose and accept trades: **

![image](https://github.com/user-attachments/assets/732af87e-a012-4ea2-8aa2-f150205beb8a)
![image](https://github.com/user-attachments/assets/5ba6f962-2020-4c06-b53b-9945fc924b3f)



