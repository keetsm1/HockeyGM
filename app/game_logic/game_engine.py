import random
from datetime import date,timedelta
from .sqldb import fetch_team_roster, fetch_all_team_names, fetch_team_roster_full, save_player_stats, save_team_stats


class GameEngine:
    PERIODS= 3
    PERIOD_LENGTH= 20
    OVERTIME_LENGTH= 5
    GOAL_PER_MINS= 0.05
    OT_GOALS_PER_MIN=0.05

    def get_all_teams(self):
        return fetch_all_team_names()

    def calculate_ratings(self, team):
        skaters = []
        for player in team:
            if player.get('Position') != 'G':
                skaters.append(player)

        goalies = []
        for player in team:
            if player.get('Position') == 'G':
                goalies.append(player)

        # OFFENSE
        offense_values = []
        for p in skaters:
            shooting = p.get('Shooting') or 0
            vision = p.get('Vision') or 0
            speed = p.get('Speed') or 0

            individual_value = 0.6 * shooting + 0.4 * vision + 0.2 * speed
            offense_values.append(individual_value)

        average_offense = sum(offense_values) / max(len(offense_values), 1)

        # DEFENSE
        defense_values = []
        for p in skaters:
            # If any of these is None, default to 0
            defense_attribute_dman = p.get("Defense") or 0
            defense_attribute_oman = p.get("Forward Defense") or 0
            skating = p.get("Skating") or 0

            total_defense = (
                    0.7 * defense_attribute_dman
                    + 0.3 * defense_attribute_oman
                    + 0.4 * skating
            )
            defense_values.append(total_defense)

        average_defense = sum(defense_values) / max(len(defense_values), 1)

        # GOALIES
        goalies_defense = []
        for goalie in goalies:
            glove = goalie.get('Glove') or 0
            block = goalie.get('Blocker') or 0
            rebound = goalie.get('Rebound') or 0
            composure = goalie.get('Composure') or 0

            average_gk = (glove + block + rebound + composure) / 4
            goalies_defense.append(average_gk)

        avg_goalie_def = sum(goalies_defense) / max(len(goalies_defense), 1)
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
        first_team=fetch_team_roster_full(team1)
        second_team= fetch_team_roster_full(team2)

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

    def generate_regular_season_schedule(self):
        # 0) Fetch all teams once, and guard against None.
        raw_teams = fetch_all_team_names()
        if not raw_teams:
            raise RuntimeError("fetch_all_team_names() returned no teams (None or empty).")

        # 1) Exclude “FREE AGENT” if present (singular, not “FREE AGENTS”)
        teams = [t for t in raw_teams if t != "FREE AGENT"]
        if len(teams) < 2:
            raise RuntimeError("Need at least two real teams to build a schedule.")

        # 2) Build a single round-robin (each team plays every other team once)
        first_half = self.round_robin(teams)

        # 3) Flatten into a list of (home, away) tuples
        first_half_games = []
        for round_games in first_half:
            for (home, away) in round_games:
                first_half_games.append((home, away))

        # 4) Create the second half by swapping home/away
        second_half_games = [(away, home) for (home, away) in first_half_games]

        # 5) Combine → each team has (N−1)*2 games so far
        all_games = first_half_games + second_half_games

        # 6) Add 20 extra games per team (10 home, 10 away) for 82 total
        for team in teams:
            opponents = [t for t in teams if t != team]
            random.shuffle(opponents)
            extra_opponents = opponents[:20]

            for idx, opp in enumerate(extra_opponents):
                if idx < 10:
                    # team is home
                    all_games.append((team, opp))
                else:
                    # team is away
                    all_games.append((opp, team))

        # 7) Shuffle all matchups
        random.shuffle(all_games)

        # 8) Spread games between Oct 1, 2025 → Apr 17, 2026
        season_start = date(2025, 10, 1)
        season_end = date(2026, 4, 17)
        total_days = (season_end - season_start).days  # 199
        total_games = len(all_games)  # 1312

        days_list = [season_start + timedelta(days=d) for d in range(total_days + 1)]
        busy_teams = [set() for _ in range(total_days + 1)]
        schedule = []

        for i, (home, away) in enumerate(all_games):
            ideal_idx = (i * total_days) // (total_games - 1)

            placed = False
            # Try ideal day or later
            for j in range(ideal_idx, total_days + 1):
                if (home not in busy_teams[j]) and (away not in busy_teams[j]):
                    busy_teams[j].add(home)
                    busy_teams[j].add(away)
                    schedule.append((days_list[j], home, away))
                    placed = True
                    break

            if not placed:
                # Wrap around
                for j in range(0, ideal_idx):
                    if (home not in busy_teams[j]) and (away not in busy_teams[j]):
                        busy_teams[j].add(home)
                        busy_teams[j].add(away)
                        schedule.append((days_list[j], home, away))
                        placed = True
                        break

            if not placed:
                raise RuntimeError(f"Unable to schedule {home} vs {away}—no free day found.")

        return schedule

    def round_robin(self, teams):
        pool = teams[:]
        if len(pool) % 2 == 1:
            pool.append("BYE")

        n = len(pool)
        schedule = []

        for _ in range(n - 1):
            pairings = []
            for i in range(n // 2):
                t1, t2 = pool[i], pool[n - 1 - i]
                if t1 != "BYE" and t2 != "BYE":
                    pairings.append((t1, t2))
            schedule.append(pairings)

            # Rotate (keep pool[0] fixed)
            pool = [pool[0]] + [pool[-1]] + pool[1:-1]

        return schedule

    def start_season(self):
        self.schedule= self.generate_regular_season_schedule()
        self.current_game_id= 0
        self.stats= {}

        for t in fetch_all_team_names():
            self.stats[t] = {"W": 0, "L": 0, "OTL": 0, "PTS": 0}

    def simulate_next_game(self):
        game_date, home, away = self.schedule[self.current_game_id]

        # 2) Run simulation
        outcome = self.simulate_game(home, away)
        winner = outcome['winner']
        loser = outcome['loser']
        ot = outcome['overtime']

        # 3) Update in‐memory standings
        self.stats[winner]['W'] += 1
        self.stats[winner]['PTS'] += 2

        if ot:
            self.stats[loser]['OTL'] += 1
            self.stats[loser]['PTS'] += 1
        else:
            self.stats[loser]['L'] += 1

        winner_W = self.stats[winner]['W']
        winner_L=self.stats[winner]['L']
        winner_PTS= self.stats[winner]['PTS']
        winner_OTL= self.stats[winner]['OTL']
        save_team_stats(winner,winner_W,winner_L,winner_OTL,winner_PTS)

        loser_W = self.stats[loser]['W']
        loser_L = self.stats[loser]['L']
        loser_PTS = self.stats[loser]['PTS']
        loser_OTL = self.stats[loser]['OTL']
        save_team_stats(loser, loser_W, loser_L, loser_OTL,loser_PTS)

        # 4) Tally goals, assists, and points per individual player from this game’s events
        player_goal_counts = {}
        player_assist_counts = {}

        for ev in outcome['events']:
            scorer = ev['scorer']
            assist1 = ev['assist1']
            assist2 = ev['assist2']

            # Increment the goal‐counter for the scorer
            if scorer not in player_goal_counts:
                player_goal_counts[scorer] = 0
            player_goal_counts[scorer] += 1

            # Increment the assist‐counters
            if assist1:
                if assist1 not in player_assist_counts:
                    player_assist_counts[assist1] = 0
                player_assist_counts[assist1] += 1
            if assist2:
                if assist2 not in player_assist_counts:
                    player_assist_counts[assist2] = 0
                player_assist_counts[assist2] += 1

        all_scorers_and_assisters = set(player_goal_counts.keys()) | set(player_assist_counts.keys())

        for player_name in all_scorers_and_assisters:
            goals = player_goal_counts.get(player_name, 0)
            assists = player_assist_counts.get(player_name, 0)
            points = goals + assists

            # Determine team by checking home roster first
            first_team_names = [p['Name'] for p in fetch_team_roster_full(home)]
            if player_name in first_team_names:
                team_name = home
            else:
                team_name = away

            save_player_stats(player_name, team_name, goals, assists, points)

        self.current_game_id += 1

        return game_date, home, away, outcome

    def get_remaining_games(self):
        return self.schedule[self.current_game_id:]

    def get_standings(self):
        table = [(team, s) for team, s in self.stats.items()]
        table.sort(key=lambda item: (item[1]['PTS'], item[1]['W']), reverse=True)
        return table

