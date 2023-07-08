from team.team_generator import TeamGenerator
import numpy as np

BATTING_CHOICES = [1, 2, 3, 4, 5, 6]
BATTING_PROBABILITIES = [0.55, 0.1, 0.1, 0.1, 0.1, 0.05]

BOWLING_CHOICES = [1, 2, 3, 4]
BOWLING_PROBABILITIES = [0.75, 0.1, 0.1, 0.05]

batting_schema = {
        1: 1, #one
        2: 2, #two
        3: 3, #three
        4: 4, #four
        5: 0, #out
        6: 6 #six
    }

bowling_schema = {
    1: 0, #ball
    2: 1, #wide
    3: 1, #no_ball
    4: 0, #bouncer
}

team1_generator = TeamGenerator("Sunrisers", "players.csv")
team1 = team1_generator.generate_teams()

team2_generator = TeamGenerator("Challengers", "players_two.csv")
team2 = team2_generator.generate_teams()

num_overs = 20
score = 0
total_balls = num_overs * 6
remaining_balls = total_balls

batsman = team1.players[0]
index = 1

bowler = team2.players[0]

while(remaining_balls > 0):
    batting_chc = np.random.choice(BATTING_CHOICES, p=BATTING_PROBABILITIES)
    bowling_chc = np.random.choice(BOWLING_CHOICES, p=BOWLING_PROBABILITIES)

    print(batting_chc, bowling_chc)
    if batting_chc == 5:
        print(f"{batsman.name} is out")
        batsman.is_out = True
        team1.players[index - 1] = batsman
        batsman = team1.players[index]
        
        # to check if all players have been taken out
        if index + 1 < len(team1.players):
            index += 1
        else:
            print("All players have been taken out.")
            print(f"Total score by {team1.team_name} = {score}, remaining balls = {remaining_balls}")
            break
    elif(bowling_chc == 1):
        score += batting_schema[batting_chc]
    else:
        score += bowling_schema[bowling_chc]
        remaining_balls += 1 # so that our ball is not counted

    remaining_balls -= 1