from team.team_generator import TeamGenerator
import numpy as np

BATTING_CHOICES = [1, 2, 3, 4, 5, 6]
BATTING_PROBABILITIES = [0.5, 0.15, 0.1, 0.1, 0.1, 0.05]

BOWLING_CHOICES = [1, 2, 3, 4, 5]
BOWLING_PROBABILITIES = [0.7, 0.1, 0.1, 0.05, 0.05]

team1_generator = TeamGenerator("Sunrisers", "players.csv")
team1 = team1_generator.generate_teams()

team2_generator = TeamGenerator("Challengers", "players_two.csv")
team2 = team2_generator.generate_teams()

num_overs = 20
score = 0
total_balls = num_overs * 6
remaining_balls = total_balls

batsman = team1.players[0]
runner = team1.players[1]

bowler = team2.players[0]

while(remaining_balls > 0):
    batting_schema = {
        1: 1, #one
        2: 2, #two
        3: 3, #three
        4: 4, #four
        5: -1, #out
        6: 6 #six
    }

    bowling_schema = {
        1: 0, #ball
        2: 0, #wide
        3: 1, #no_ball
        4: 0, #bouncer
        5: 0 #lbw
    }

    batting_chc = np.random.choice(BATTING_CHOICES, p=BATTING_PROBABILITIES)
    bowling_chc = np.random.choice(BOWLING_CHOICES, p=BOWLING_PROBABILITIES)

    print(batting_chc, bowling_chc)

    if(batsman.is_out):
        pass

    break