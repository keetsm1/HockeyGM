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
            player.position= random("LW","C","RW")

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





