import csv
import random
from random import randint

class player_generation:
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
        with open('first_names.csv', mode= 'r') as file:
            reader= csv.DictReader(file)
            first_names= [row['first_name'] for row in reader]

        with open('last_names.csv',mode = 'r') as file:
            reader = csv.DictReader(file)
            last_names = [row['last_names'] for row in reader]


        total_forwards= 750

        elite_forward_probability= int(0.05 *total_forwards)

        for _ in range(elite_forward_probability):
            player= player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player.potential= "Elite"
            player.age= randint(18,35)
            player.height= randint(172, 195) #in centimeters
            player.position= random.choice(["LW","C","RW"])

            if (player.age == 18 or player.age == 19 or player.age== 20 or player.age==21):
                player.weight= randint(140,180) #in lbs
            else:
                player.weight= randint(160, 220)

            player.shooting= randint(80,93)
            player.determination = randint(75,90)
            player.passing= randint(80,94)
            player.vision= randint(80,95)
            player.dman_defense = 0
            player.forward_defense = randint(60,90)
            player.skating = randint(70,95)
            player.speed= randint(70,95)

            #--------------------------------------------------------------------------------------------------------
            top6_forward_probability = int(0.15 * total_forwards)

            for _ in range(top6_forward_probability):
                player = player_generation()
                first = random.choice(first_names)
                last = random.choice(last_names)
                player.name = f"{first} {last}"
                player.potential = "Top 6"
                player.age = randint(18, 35)
                player.height = randint(172, 195)  # in centimeters
                player.position = random.choice(["LW", "C", "RW"])

                if (player.age == 18 or player.age == 19 or player.age == 20 or player.age == 21):
                    player.weight = randint(140, 180)  # in lbs
                else:
                    player.weight = randint(160, 220)

                player.shooting = randint(70, 90)
                player.determination = randint(65, 85)
                player.passing = randint(70, 90)
                player.vision = randint(65, 88)
                player.dman_defense = 0
                player.forward_defense = randint(60, 90)
                player.skating = randint(60, 90)
                player.speed = randint(70, 95)

                # --------------------------------------------------------------------------------------------------------
                bottom6_forward_probability = int(0.30 * total_forwards)

                for _ in range(bottom6_forward_probability):
                    player = player_generation()
                    first = random.choice(first_names)
                    last = random.choice(last_names)
                    player.name = f"{first} {last}"
                    player.potential = "Bottom 6"
                    player.age = randint(18, 35)
                    player.height = randint(172, 195)  # in centimeters
                    player.position = random.choice(["LW", "C", "RW"])

                    if (player.age == 18 or player.age == 19 or player.age == 20 or player.age == 21):
                        player.weight = randint(140, 180)  # in lbs
                    else:
                        player.weight = randint(160, 220)

                    player.shooting = randint(60, 82)
                    player.determination = randint(50, 70)
                    player.passing = randint(60, 83)
                    player.vision = randint(60, 88)
                    player.dman_defense = 0
                    player.forward_defense = randint(60, 85)
                    player.skating = randint(60, 90)
                    player.speed = randint(50, 95)

                    # --------------------------------------------------------------------------------------------------------
                    fringe_player_probability = int(0.25 * total_forwards)

                    for _ in range(fringe_player_probability):
                        player = player_generation()
                        first = random.choice(first_names)
                        last = random.choice(last_names)
                        player.name = f"{first} {last}"
                        player.potential = "Fringe Player"
                        player.age = randint(18, 35)
                        player.height = randint(172, 195)  # in centimeters
                        player.position = random.choice(["LW", "C", "RW"])

                        if (player.age == 18 or player.age == 19 or player.age == 20 or player.age == 21):
                            player.weight = randint(140, 180)  # in lbs
                        else:
                            player.weight = randint(160, 220)

                        player.shooting = randint(30, 60)
                        player.determination = randint(40, 65)
                        player.passing = randint(35, 65)
                        player.vision = randint(40, 68)
                        player.dman_defense = 0
                        player.forward_defense = randint(45, 70)
                        player.skating = randint(40, 75)
                        player.speed = randint(40, 75)

    def generate_defenseman(self):
        with open('first_names.csv', mode= 'r') as file:
            reader= csv.DictReader(file)
            first_names= [row['first_name'] for row in reader]

        with open('last_names.csv',mode = 'r') as file:
            reader = csv.DictReader(file)
            last_names = [row['last_names'] for row in reader]


        total_defenseman= 330

        elite_defenseman_probability= int(0.05 *total_defenseman)

        for _ in range(elite_defenseman_probability):
            player= player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player.potential= "Elite"
            player.age= randint(18,35)
            player.height= randint(172, 195) #in centimeters
            player.position= random.choice(["LD","RD","LD/RD"])

            if (player.age == 18 or player.age == 19 or player.age== 20 or player.age==21):
                player.weight= randint(145,200) #in lbs
            else:
                player.weight= randint(170, 240)

            player.shooting= randint(75,90)
            player.determination = randint(80,95)
            player.passing= randint(73,94)
            player.vision= randint(80,95)
            player.dman_defense = randint(85,98)
            player.forward_defense = 0
            player.skating = randint(80,95)
            player.speed= randint(75,95)

            #--------------------------------------------------------------------------------------------------------
            top4_dman_probability = int(0.15 * total_defenseman)

            for _ in range(top4_dman_probability):
                player = player_generation()
                first = random.choice(first_names)
                last = random.choice(last_names)
                player.name = f"{first} {last}"
                player.potential = "Top 4"
                player.age = randint(18, 35)
                player.height = randint(172, 195)  # in centimeters
                player.position = random.choice(["LD", "RD", "LD/RD"])

                if (player.age == 18 or player.age == 19 or player.age == 20 or player.age == 21):
                    player.weight = randint(145, 185)  # in lbs
                else:
                    player.weight = randint(165, 230)

                player.shooting = randint(65, 83)
                player.determination = randint(65, 85)
                player.passing = randint(70, 85)
                player.vision = randint(60, 85)
                player.dman_defense = randint(75,90)
                player.forward_defense = 0
                player.skating = randint(60, 88)
                player.speed = randint(70, 85)

                # --------------------------------------------------------------------------------------------------------
                bottom4_dman_probability = int(0.30 * total_defenseman)

                for _ in range(bottom4_dman_probability):
                    player = player_generation()
                    first = random.choice(first_names)
                    last = random.choice(last_names)
                    player.name = f"{first} {last}"
                    player.potential = "Bottom 4"
                    player.age = randint(18, 35)
                    player.height = randint(172, 195)  # in centimeters
                    player.position = random.choice(["LD", "RD", "LD/RD"])

                    if (player.age == 18 or player.age == 19 or player.age == 20 or player.age == 21):
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

                    # --------------------------------------------------------------------------------------------------------
                    fringe_dman_probability = int(0.25 * total_defenseman)

                    for _ in range(fringe_dman_probability):
                        player = player_generation()
                        first = random.choice(first_names)
                        last = random.choice(last_names)
                        player.name = f"{first} {last}"
                        player.potential = "Fringe Player"
                        player.age = randint(18, 35)
                        player.height = randint(172, 195)  # in centimeters
                        player.position = random.choice(["LD", "RD", "LD/RD"])

                        if (player.age == 18 or player.age == 19 or player.age == 20 or player.age == 21):
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


    def generate_goalies(self):
        total_goalies=80

        with open('first_names.csv', mode= 'r') as file:
            reader= csv.DictReader(file)
            first_names= [row['first_name'] for row in reader]

        with open('last_names.csv',mode = 'r') as file:
            reader = csv.DictReader(file)
            last_names = [row['last_names'] for row in reader]

        elite_goalies_probability = int(0.06 * total_goalies)

        for _ in range(elite_goalies_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
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

        #--------------------------------------------------------------------------------------------------------
        starter_goalies_probability = int(0.28 * total_goalies)

        for _ in range(starter_goalies_probability):
            player = player_generation()
            first = random.choice(first_names)
            last = random.choice(last_names)
            player.name = f"{first} {last}"
            player.potential = "Starter"
            player.age = randint(18, 35)
            player.height = randint(172, 195)  # in centimeters
            player.position = "G"

            if (player.age == 18 or player.age == 19 or player.age == 20 or player.age == 21):
                player.weight = randint(145, 200)  # in lbs
            else:
                player.weight = randint(170, 220)

            player.rebound_control = randint(75, 88)
            player.technique = randint(78, 90)
            player.glove = randint(77, 90)
            player.blocker = randint(75, 88)
            player.puck_handling = randint(60, 75)
            player.composure = randint(75, 90)
        #-------------------------------------------------------------------------------------------------------------
        backup_goalies_probability= int(0.35*total_goalies)
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
        #---------------------------------------------------------------------------------------------------------------
        fringe_goalie_probability= int(0.30 *total_goalies)
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









