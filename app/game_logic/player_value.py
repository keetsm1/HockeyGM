from . import player_gen

class playerValue(player_gen.player_generation):
    def __init__(self,name,position,potential,age,overall_rating):
        super().__init__()
        self.name= name
        self.position= position
        self.potential = potential
        self.age= age
        self.overall_rating= overall_rating

    def calculate_value(self):
        player_value= 0

        if self.age<23:
            player_value= player_value+10
        elif self.age>32:
            player_value -= -15
        elif self.age>35:
            player_value -= -20

        if self.potential == "Low Elite":
            player_value=player_value+20
        elif self.potential == "Medium Elite":
            player_value= player_value+30
        elif self.potential == "Elite":
            player_value = player_value+50
        elif self.potential == "Low Top 6":
            player_value = player_value +10
        elif self.potential == "Medium Top 6":
            player_value = player_value +15
        elif self.potential == "High Top 6":
            player_value = player_value +25
        elif self.potential == "High Top 4":
            player_value += 25
        elif self.potential == "Medium Top 4":
            player_value+= 20
        elif self.potential == "Low Top 4":
            player_value += 15
        elif self.potential == "Starter":
            player_value+= 20
        elif self.potential == "Medium Starter":
            player_value += 13
        elif self.potential == "Low Starter":
            player_value += 8
        elif self.potential == "Backup":
            player_value+= 3

        if self.overall_rating> 95:
            player_value+= 50
        elif self.overall_rating> 80 and self.overall_rating<95:
            player_value+= 35
        elif self.overall_rating> 70 and self.overall_rating<80:
            player_value+= 15
        else:
            player_value+=5

        return player_value

    def isTradeFair(team1_data, team2_data, threshold=10):


        total1 = sum(p.calculate_value() for p in team1_data)
        total2 = sum(p.calculate_value() for p in team2_data)

        if total1 >= total2:
            return True

        if (total1 - total2) <= threshold:
            return True

        return False


