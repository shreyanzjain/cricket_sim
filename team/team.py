from team.teamInterace import ITeam
from player import Player
from typing import List

class Team(ITeam):

    def __init__(self, team_name: str, players: List[Player]):
        self.team_name = team_name
        self.players = players
        self.captian = self.players[0]

    def generate_batting_order(self):
        pass
    
    def generate_bowling_order(self):
        pass

    def select_captain(self):
        for player in self.players:
            if player.experience > self.captian.experience:
                self.captian = player
        
        print(f"{self.team_name} captain set to: {self.captian.name}")

    def send_player(self):
        pass

    def choose_bowler():
        pass
