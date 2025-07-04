import csv
import random
import os
from random import randint
from app.game_logic.sqldb import save_to_database

# Path constants for name CSV files
BASE_DIR = os.path.dirname(__file__)
FIRST_NAMES_FILE = os.path.join(BASE_DIR, 'first_names.csv')
LAST_NAMES_FILE = os.path.join(BASE_DIR, 'last_names.csv')

def load_name_lists():
    """
    Load first and last names from CSV files and return two lists.
    """
    with open(FIRST_NAMES_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        first_names = [row['first_name'] for row in reader]
    with open(LAST_NAMES_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        # Note: header in CSV is 'last_name'
        last_names = [row.get('last_names', row.get('last_name')) for row in reader]
    return first_names, last_names

class player_generation:
    SALARY_CAP= 95_500_000
    def __init__(self):
        self.name= ""
        self.potential= ""
        self.age= 0
        self.weight=0
        self.height= 0
        self.position= " "
        #after this, player attributes
        self.shooting=0
        self.determination=0
        self.passing= 0
        self.vision=0
        self.dman_defense= 0
        self.forward_defense=0
        self.skating = 0
        self.speed=0
        #for goalies:
        self.rebound_control=0
        self.technique=0 #pad saves
        self.glove= 0
        self.blocker=0
        self.puck_handling=0
        self.composure=0

    def generate_forwards(self):
        first_names, last_names = load_name_lists()

        total_forwards = 750

        elite_forward_probability = round(0.10 * total_forwards)
        top6_forward_probability = round(0.2 * total_forwards)
        bottom6_forward_probability = round(0.35 * total_forwards)
        fringe_player_probability = round(0.45 * total_forwards)

        generated_players = []

        # ----- Elite Forwards -----
        for _ in range(elite_forward_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"

            r = random.randint(1, 100)
            if r <= 25:
                player.potential = "Low Elite"
            elif r <= 75:
                player.potential = "Medium Elite"
            else:
                player.potential = "Elite"

            player.age = random.randint(18, 35)
            player.height = random.randint(172, 195)
            player.position = random.choice(["LW", "C", "RW"])
            player.weight = (random.randint(140, 180)
                             if player.age <= 21
                             else random.randint(160, 220))

            player.shooting = random.randint(80, 93)
            player.determination = random.randint(75, 90)
            player.passing = random.randint(80, 94)
            player.vision = random.randint(80, 95)
            player.dman_defense = 0
            player.forward_defense = random.randint(60, 90)
            player.skating = random.randint(70, 95)
            player.speed = random.randint(70, 95)

            generated_players.append(player)

        # ----- Top‑6 Forwards -----
        for _ in range(top6_forward_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"

            r = random.randint(1, 100)
            if r <= 25:
                player.potential = "Low Top 6"
            elif r <= 75:
                player.potential = "Medium Top 6"
            else:
                player.potential = "Top 6"

            player.age = random.randint(18, 35)
            player.height = random.randint(172, 195)
            player.position = random.choice(["LW", "C", "RW"])
            player.weight = (random.randint(140, 180)
                             if player.age <= 21
                             else random.randint(160, 220))

            player.shooting = random.randint(70, 90)
            player.determination = random.randint(65, 85)
            player.passing = random.randint(70, 90)
            player.vision = random.randint(65, 88)
            player.dman_defense = 0
            player.forward_defense = random.randint(60, 90)
            player.skating = random.randint(60, 90)
            player.speed = random.randint(70, 95)

            generated_players.append(player)

        # ----- Bottom‑6 Forwards -----
        for _ in range(bottom6_forward_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"

            r = random.randint(1, 100)
            if r <= 25:
                player.potential = "Low Bottom 6"
            elif r <= 75:
                player.potential = "Medium Bottom 6"
            else:
                player.potential = "High Bottom 6"

            player.age = random.randint(18, 35)
            player.height = random.randint(172, 195)
            player.position = random.choice(["LW", "C", "RW"])
            player.weight = (random.randint(140, 180)
                             if player.age <= 21
                             else random.randint(160, 220))

            player.shooting = random.randint(60, 82)
            player.determination = random.randint(50, 70)
            player.passing = random.randint(60, 83)
            player.vision = random.randint(60, 88)
            player.dman_defense = 0
            player.forward_defense = random.randint(60, 85)
            player.skating = random.randint(60, 90)
            player.speed = random.randint(50, 95)

            generated_players.append(player)

        # ----- Fringe Forwards -----
        for _ in range(fringe_player_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"

            r = random.randint(1, 100)
            if r <= 25:
                player.potential = "Low Fringe"
            elif r <= 75:
                player.potential = "Medium Fringe"
            else:
                player.potential = "Fringe"

            player.age = random.randint(18, 35)
            player.height = random.randint(172, 195)
            player.position = random.choice(["LW", "C", "RW"])
            player.weight = (random.randint(140, 180)
                             if player.age <= 21
                             else random.randint(160, 220))

            player.shooting = random.randint(30, 60)
            player.determination = random.randint(40, 65)
            player.passing = random.randint(35, 65)
            player.vision = random.randint(40, 68)
            player.dman_defense = 0
            player.forward_defense = random.randint(45, 70)
            player.skating = random.randint(40, 75)
            player.speed = random.randint(40, 75)

            generated_players.append(player)

        return generated_players

    def generate_defenseman(self):
        first_names, last_names = load_name_lists()

        generated_players = []

        total_defenseman = 500

        elite_defenseman_probability = int(0.1 * total_defenseman)
        top4_dman_probability = int(0.2 * total_defenseman)
        bottom4_dman_probability = int(0.35 * total_defenseman)
        fringe_dman_probability = int(0.45 * total_defenseman)

        # Elite
        for _ in range(elite_defenseman_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player_reaching_potential = randint(0, 100)

            if player_reaching_potential <= 25:
                player.potential = "Low Elite"
            elif player_reaching_potential > 25 and player_reaching_potential <= 75:
                player.potential = "Medium Elite"
            else:
                player.potential = "Elite"

            player.age = randint(18, 35)
            player.height = randint(172, 195)  # in centimeters
            player.position = random.choice(["LD", "RD", "LD/RD"])

            if player.age in (18, 19, 20, 21):
                player.weight = randint(145, 200)  # in lbs
            else:
                player.weight = randint(170, 240)

            player.shooting = randint(75, 90)
            player.determination = randint(80, 95)
            player.passing = randint(73, 94)
            player.vision = randint(80, 95)
            player.dman_defense = randint(85, 98)
            player.forward_defense = 0
            player.skating = randint(80, 95)
            player.speed = randint(75, 95)

            generated_players.append(player)

        # Top‑4
        for _ in range(top4_dman_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player_reaching_potential = randint(1, 100)

            if player_reaching_potential <= 25:
                player.potential = "Low Top 4"
            elif player_reaching_potential <= 75:
                player.potential = "Medium Top 4"
            else:
                player.potential = "High Top 4"

            player.age = randint(18, 35)
            player.height = randint(172, 195)  # in centimeters
            player.position = random.choice(["LD", "RD", "LD/RD"])

            if player.age in (18, 19, 20, 21):
                player.weight = randint(145, 185)  # in lbs
            else:
                player.weight = randint(165, 230)

            player.shooting = randint(65, 83)
            player.determination = randint(65, 85)
            player.passing = randint(70, 85)
            player.vision = randint(60, 85)
            player.dman_defense = randint(75, 90)
            player.forward_defense = 0
            player.skating = randint(60, 88)
            player.speed = randint(70, 85)

            generated_players.append(player)

        # Bottom‑4
        for _ in range(bottom4_dman_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player_reaching_potential = randint(0, 100)

            if player_reaching_potential <= 25:
                player.potential = "Low Bottom 4"
            elif player_reaching_potential > 25 and player_reaching_potential <= 75:
                player.potential = " Medium Bottom 4"
            else:
                player.potential = "Bottom 4"

            player.age = randint(18, 35)
            player.height = randint(172, 195)  # in centimeters
            player.position = random.choice(["LD", "RD", "LD/RD"])

            if player.age in (18, 19, 20, 21):
                player.weight = randint(140, 180)  # in lbs
            else:
                player.weight = randint(160, 220)

            player.shooting = randint(55, 75)
            player.determination = randint(50, 70)
            player.passing = randint(55, 78)
            player.vision = randint(55, 80)
            player.dman_defense = randint(65, 80)
            player.forward_defense = 0
            player.skating = randint(60, 85)
            player.speed = randint(55, 85)

            generated_players.append(player)

        # Fringe
        for _ in range(fringe_dman_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player_reaching_potential = randint(0, 100)

            if player_reaching_potential <= 25:
                player.potential = "Low Fringe"
            elif player_reaching_potential > 25 and player_reaching_potential <= 75:
                player.potential = "Medium Fringe "
            else:
                player.potential = "Fringe"

            player.age = randint(18, 35)
            player.height = randint(172, 195)  # in centimeters
            player.position = random.choice(["LD", "RD", "LD/RD"])

            if player.age in (18, 19, 20, 21):
                player.weight = randint(140, 180)  # in lbs
            else:
                player.weight = randint(160, 220)

            player.shooting = randint(30, 58)
            player.determination = randint(40, 62)
            player.passing = randint(35, 60)
            player.vision = randint(38, 65)
            player.dman_defense = randint(55, 70)  # Not great defensively
            player.forward_defense = 0
            player.skating = randint(40, 72)
            player.speed = randint(40, 72)

            generated_players.append(player)

        return generated_players

    def generate_goalies(self):
        total_goalies = 120

        first_names, last_names = load_name_lists()

        generated_players = []

        elite_goalies_probability = int(0.06 * total_goalies)
        for _ in range(elite_goalies_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player_reaching_potential = randint(0, 100)

            if player_reaching_potential <= 25:
                player.potential = "Low Elite"
            elif player_reaching_potential > 25 and player_reaching_potential <= 75:
                player.potential = "Medium Elite"
            else:
                player.potential = "Elite"
            player.age = randint(18, 35)
            player.height = randint(172, 195)  # in centimeters
            player.position = "G"

            if (player.age == 18 or player.age == 19 or player.age == 20 or player.age == 21):
                player.weight = randint(145, 200)  # in lbs
            else:
                player.weight = randint(170, 220)

            player.rebound_control = randint(85, 95)
            player.technique = randint(88, 97)
            player.glove = randint(87, 96)
            player.blocker = randint(86, 95)
            player.puck_handling = randint(70, 85)
            player.composure = randint(88, 98)

            generated_players.append(player)

        # --------------------------------------------------------------------------------------------------------
        starter_goalies_probability = int(0.28 * total_goalies)
        for _ in range(starter_goalies_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player_reaching_potential = randint(0, 100)

            if player_reaching_potential <= 25:
                player.potential = "Low Starter"
            elif player_reaching_potential > 25 and player_reaching_potential <= 75:
                player.potential = "Medium Starter"
            else:
                player.potential = "Starter"
            player.age = randint(18, 35)
            player.height = randint(172, 195)  # in centimeters
            player.position = "G"

            if (player.age <= 21):
                player.weight = randint(145, 200)  # in lbs
            else:
                player.weight = randint(170, 220)

            player.rebound_control = randint(75, 88)
            player.technique = randint(78, 90)
            player.glove = randint(77, 90)
            player.blocker = randint(75, 88)
            player.puck_handling = randint(60, 75)
            player.composure = randint(75, 90)

            generated_players.append(player)

        # -------------------------------------------------------------------------------------------------------------
        backup_goalies_probability = int(0.35 * total_goalies)
        for _ in range(backup_goalies_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player.potential = "Backup"
            player.age = randint(18, 35)
            player.height = randint(172, 195)  # in centimeters
            player.position = "G"

            if (player.age == 18 or player.age == 19 or player.age == 20 or player.age == 21):
                player.weight = randint(145, 200)  # in lbs
            else:
                player.weight = randint(170, 220)

            player.rebound_control = randint(65, 80)
            player.technique = randint(68, 82)
            player.glove = randint(65, 82)
            player.blocker = randint(65, 80)
            player.puck_handling = randint(50, 70)
            player.composure = randint(65, 80)

            generated_players.append(player)

        # ---------------------------------------------------------------------------------------------------------------
        fringe_goalie_probability = int(0.30 * total_goalies)
        for _ in range(fringe_goalie_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player.potential = "Fringe"
            player.age = randint(18, 35)
            player.height = randint(172, 195)  # in centimeters
            player.position = "G"

            if (player.age == 18 or player.age == 19 or player.age == 20 or player.age == 21):
                player.weight = randint(145, 200)  # in lbs
            else:
                player.weight = randint(170, 220)

            player.rebound_control = randint(50, 68)
            player.technique = randint(55, 70)
            player.glove = randint(50, 72)
            player.blocker = randint(50, 70)
            player.puck_handling = randint(40, 60)
            player.composure = randint(50, 68)
            generated_players.append(player)

        return generated_players

    def overall_rating_offense(self):
        overall= (self.shooting+ self.passing+ self.vision+self.forward_defense+self.skating+self.speed)/6

        return round(overall)

    def overall_rating_defense(self):
        overall = (self.shooting + self.passing + self.vision + self.dman_defense + self.skating + self.speed) / 6

        return round(overall)

    def overall_rating_goalies(self):
        overall = (self.rebound_control+ self.technique+ self.glove+ self.blocker+ self.puck_handling+ self.composure) / 6

        return round(overall)

    def generate_salary(self, overall_rating):
        if overall_rating >= 90:
            low, high = 8_000_000, 12_000_000
        elif overall_rating >= 88:
            low, high = 7_000_000, 8_000_000
        elif overall_rating >= 86:
            low, high = 3_500_000, 6_500_000
        elif overall_rating >= 83:
            low, high = 2_500_000, 3_500_000
        elif overall_rating >= 80:
            low, high = 2_000_000, 2_500_000
        elif overall_rating >= 70:
            low, high = 725_000, 2_000_000
        else:
            low, high = 725_000, 1_000_000

        return randint(low, high)

    def salary_range(self, overall_rating):
        if overall_rating >= 90:
            return 8_000_000, 12_000_000
        elif overall_rating >= 88:
            return 7_000_000, 8_000_000
        elif overall_rating >= 86:
            return 3_500_000, 6_500_000
        elif overall_rating >= 83:
            return 2_500_000, 3_500_000
        elif overall_rating >= 80:
            return 2_000_000, 2_500_000
        elif overall_rating >= 70:
            return   725_000, 2_000_000
        else:
            return   725_000, 1_000_000

    def create_players(self):
        NHL_TEAMS = [
            "Anaheim Ducks", "Arizona Coyotes", "Boston Bruins", "Buffalo Sabres",
            "Calgary Flames", "Carolina Hurricanes", "Chicago Blackhawks", "Colorado Avalanche",
            "Columbus Blue Jackets", "Dallas Stars", "Detroit Red Wings", "Edmonton Oilers",
            "Florida Panthers", "Los Angeles Kings", "Minnesota Wild", "Montreal Canadiens",
            "Nashville Predators", "New Jersey Devils", "New York Islanders", "New York Rangers",
            "Ottawa Senators", "Philadelphia Flyers", "Pittsburgh Penguins", "San Jose Sharks",
            "Seattle Kraken", "St. Louis Blues", "Tampa Bay Lightning", "Toronto Maple Leafs",
            "Vancouver Canucks", "Vegas Golden Knights", "Washington Capitals", "Winnipeg Jets"
        ]

        # 2) Generate all skaters & goalies
        all_forwards = self.generate_forwards()
        all_defensemen = self.generate_defenseman()
        all_goalies = self.generate_goalies()

        # 3) Sort by rating (as you had it)
        all_forwards.sort(key=lambda p: p.overall_rating_offense(), reverse=True)
        all_defensemen.sort(key=lambda p: p.overall_rating_defense(), reverse=True)
        all_goalies.sort(key=lambda p: p.overall_rating_goalies(), reverse=True)

        # 4) Distribute evenly into per-team lists
        def distribute_evenly(players, per_team, teams):
            random.shuffle(players)
            return {
                team: players[i * per_team:(i + 1) * per_team]
                for i, team in enumerate(teams)
            }

        fwds_by_team = distribute_evenly(all_forwards, 15, NHL_TEAMS)
        defs_by_team = distribute_evenly(all_defensemen, 8, NHL_TEAMS)
        glys_by_team = distribute_evenly(all_goalies, 3, NHL_TEAMS)

        # 5) Assign to each real team under the cap
        leftovers = []  # players that overflow the cap
        for team in NHL_TEAMS:
            roster = fwds_by_team[team] + defs_by_team[team] + glys_by_team[team]
            team_spend = 0
            for player in roster:
                # determine overall_rating
                if player.position == "G":
                    player.overall_rating = player.overall_rating_goalies()
                elif player.position in ("LD", "RD", "LD/RD"):
                    player.overall_rating = player.overall_rating_defense()
                else:
                    player.overall_rating = player.overall_rating_offense()

                low, high = self.salary_range(player.overall_rating)
                sal = self.generate_salary(player.overall_rating)

                remaining = self.SALARY_CAP - team_spend

                # if you can't even afford the minimum, drop to free agents
                if remaining < low:
                    leftovers.append(player)
                    continue

                # clamp to remaining cap if needed
                if sal > remaining:
                    sal = remaining

                player.salary = sal
                team_spend += sal
                player.team = team

                # save this player under the team
                save_to_database(player)

        # 6) Anyone not on a roster becomes a free agent
        used_ids = {
            id(p) for team in NHL_TEAMS
            for p in fwds_by_team[team] + defs_by_team[team] + glys_by_team[team]
            if getattr(p, 'team', None) != "FREE AGENT"
        }
        all_players = all_forwards + all_defensemen + all_goalies
        free_agents = [p for p in all_players if id(p) not in used_ids]
        free_agents += leftovers

        for fa in free_agents:
            # ––– make sure they have overall_rating –––
            if fa.position == "G":
                fa.overall_rating = fa.overall_rating_goalies()
            elif fa.position in ("LD", "RD", "LD/RD"):
                fa.overall_rating = fa.overall_rating_defense()
            else:
                fa.overall_rating = fa.overall_rating_offense()

            fa.team = "FREE AGENT"
            fa.salary = self.generate_salary(fa.overall_rating)
            save_to_database(fa)
