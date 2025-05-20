import player_gen

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

        if self.potential == "Low Elite":
            player_value=player_value+10
        elif self.potential == "Medium Elite":
            player_value= player_value+20
        elif self.potential == "Elite":
            player_value = player_value+35
        elif self.potential == "Low Top 6":
            player_value = player_value +5
        elif self.potential == "Medium Top 6":
            player_value = player_value +7
        elif self.potential == "High Top 6":
            player_value = player_value +10
        elif self.potential ==






