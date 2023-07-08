from team.team import Team
from player import Player
import pandas as pd

class TeamGenerator:

    def __init__(self, team_name: str, file_name: str):
        self.team_name = team_name
        self.file_name = file_name

    def generate_teams(self) -> Team:
        
        df = pd.read_csv(self.file_name)
        teamList = []

        for _, row in df.iterrows():
            new_player = Player(name=row["name"],
                                batting=row["batting"],
                                bowling=row["bowling"],
                                fielding=row["fielding"],
                                wicket_keeping=row["wicket_keeping"],
                                running=row["running"],
                                experience=row["experience"])
            teamList.append(new_player)

        team = Team(self.team_name, teamList)
        team.select_captain()

        return team