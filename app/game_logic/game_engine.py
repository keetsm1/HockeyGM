import random
from .sqldb import fetch_team_roster, fetch_all_team_names


class GameEngine:
    PERIODS= 3
    PERIOD_LENGTH= 20
    OVERTIME_LENGTH= 5
    GOAL_PER_MINS= 0.1
    OT_GOALS_PER_MIN=0.1

    def get_all_teams(self):
        return fetch_all_team_names()


    def calculate_ratings(self,team):
        skaters= []
        for player in team:
            if player.get('Position') != 'G':
                skaters.append(player)

        goalies= []
        for player in team:
            if player.get('Position') == 'G':
                goalies.append(player)

        offense_values= []

        for p in skaters:
            shooting = p.get('Shooting')
            vision= p.get('Vision')
            speed= p.get('Speed')

            individual_value = 0.6 * shooting + 0.4 * vision + 0.2 * speed

            offense_values.append(individual_value)

        average_offense= sum(offense_values)/ len(offense_values)

        defense_values = []

        for p in skaters:
            defense_attribute_dman = p.get("Defense")
            defense_attribute_oman= p.get("Forward Defense")
            skating = p.get("Skating")

            total_defense= 0.7 * defense_attribute_dman + 0.3 * defense_attribute_oman + 0.4 * skating

            defense_values.append(total_defense)

        average_defense = sum(defense_values)/len(defense_values)

        goalies_defense = []

        for goalie in goalies:
            glove = goalie.get('Glove')
            block= goalie.get('Blocker')
            rebound = goalie.get('Rebound')
            composure = goalie.get('Composure')
            average_gk= (glove+block+rebound+composure) /4
            goalies_defense.append(average_gk)


        avg_goalie_def= sum(goalies_defense)/len(goalies_defense)

        return average_offense, average_defense, avg_goalie_def

    def attempt_goal(self,offense,defense,rate):
        prob= (offense/defense) * rate

        return random.random() < prob

    def goal_scorer_and_assister(self,skaters):
        chance_of_scoring = []
        probability_of_scoring = 0
        for players in skaters:
            if players.get("Shooting")>= 85:
                probability_of_scoring= random.randint(35,50)
            elif players.get("Shooting")>= 75:
                probability_of_scoring= random.randint(15,25)
            else:
                probability_of_scoring= random.randint(1,15)

            chance_of_scoring.append(probability_of_scoring)

        total_scoring_chance= sum(chance_of_scoring)
        pick= random.uniform(0,total_scoring_chance)
        cumulative_chance = 0
        scorer= None

        for player, weight in zip(skaters, chance_of_scoring):
            cumulative_chance += weight
            if cumulative_chance >= pick:
                scorer = player['Name']
                break


        chance_of_first_assist = []
        probability_of_first_assist= 0

        for players in skaters:
            if players.get("Vision") >= 85:
                probability_of_first_assist = random.randint(35,45)
            elif players.get("Vision") >= 70:
                probability_of_first_assist = random.randint(15,25)
            else:
                probability_of_first_assist = random.randint(1,15)
            chance_of_first_assist.append(probability_of_first_assist)

        total_first_assist_chance = sum(chance_of_first_assist)
        pick_assist= random.uniform(0,total_first_assist_chance)
        cumulative_chance_assist= 0
        first_assist= None

        for player,weight in zip(skaters, chance_of_first_assist):
            cumulative_chance_assist+= weight
            if cumulative_chance_assist >= pick_assist:
                first_assist= player['Name']
                break

        chance_of_second_assist = []
        probability_of_second_assist = 0

        for players in skaters:
            if players.get("Vision") >=70 and players.get("Passing") >= 80:
                probability_of_second_assist = random.randint(35, 45)
            elif players.get("Vision") >= 50 and players.get("Passing")>= 70:
                probability_of_second_assist = random.randint(15, 25)
            else:
                probability_of_second_assist = random.randint(1, 15)
            chance_of_second_assist.append(probability_of_second_assist)

        total_second_assist_chance = sum(chance_of_second_assist)
        pick_second_assist = random.uniform(0, total_second_assist_chance)
        cumulative_chance_second_assist = 0
        second_assist = None

        for player, weight in zip(skaters, chance_of_second_assist):
            cumulative_chance_second_assist += weight
            if cumulative_chance_second_assist >= pick_second_assist:
                second_assist = player['Name']
                break
        return scorer,first_assist,second_assist


    def simulate_game(self, team1,team2):
        first_team=fetch_team_roster(team1)
        second_team= fetch_team_roster(team2)

        avg_off1, avg_def1, avg_gk1 = self.calculate_ratings(first_team)
        avg_off2, avg_def2, avg_gk2 = self.calculate_ratings(second_team)

        defense1 = (avg_def1 + avg_gk1) / 2
        defense2 = (avg_def2 + avg_gk2) / 2


        skaters1 = [p for p in first_team if p.get('Position') != 'G']
        skaters2 = [p for p in second_team if p.get('Position') != 'G']

        score1 = 0
        score2 = 0
        events = []

        # --- regulation time ---
        for period in range(1, self.PERIODS + 1):
            for minute in range(1, self.PERIOD_LENGTH + 1):
                # team1 attack
                if self.attempt_goal(avg_off1, defense2, self.GOAL_PER_MINS):
                    scorer, a1, a2 = self.goal_scorer_and_assister(skaters1)
                    score1 += 1
                    events.append({
                        'period': period,
                        'minute': minute,
                        'team': team1,
                        'scorer': scorer,
                        'assist1': a1,
                        'assist2': a2
                    })
                # team2 attack
                if self.attempt_goal(avg_off2, defense1, self.GOAL_PER_MINS):
                    scorer, a1, a2 = self.goal_scorer_and_assister(skaters2)
                    score2 += 1
                    events.append({
                        'period': period,
                        'minute': minute,
                        'team': team2,
                        'scorer': scorer,
                        'assist1': a1,
                        'assist2': a2
                    })

        if score1 == score2:
            for minute in range(1, self.OVERTIME_LENGTH + 1):
                if self.attempt_goal(avg_off1, defense2, self.OT_GOALS_PER_MIN):
                    scorer, a1, a2 = self.goal_scorer_and_assister(skaters1)
                    score1 += 1
                    events.append({
                        'period': 'OT',
                        'minute': minute,
                        'team': team1,
                        'scorer': scorer,
                        'assist1': a1,
                        'assist2': a2
                    })
                    break
                if self.attempt_goal(avg_off2, defense1, self.OT_GOALS_PER_MIN):
                    scorer, a1, a2 = self.goal_scorer_and_assister(skaters2)
                    score2 += 1
                    events.append({
                        'period': 'OT',
                        'minute': minute,
                        'team': team2,
                        'scorer': scorer,
                        'assist1': a1,
                        'assist2': a2
                    })
                    break

        went_to_ot = any(ev['period'] == 'OT' for ev in events)

        # decide winner and loser
        if score1 > score2:
            winner, loser = team1, team2
        else:
            winner, loser = team2, team1

        return {
            'team1': team1,
            'team2': team2,
            'score1': score1,
            'score2': score2,
            'events': events,
            'winner': winner,
            'loser': loser,
            'overtime': went_to_ot,
        }




