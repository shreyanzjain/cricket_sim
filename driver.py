from team.team_generator import TeamGenerator

team1_generator = TeamGenerator("Sunrisers", "players.csv")
team1 = team1_generator.generate_teams()

team2_generator = TeamGenerator("Challengers", "players_two.csv")
team2 = team2_generator.generate_teams()