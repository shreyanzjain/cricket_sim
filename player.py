class Player:

    def __init__(self, name: str, batting: float, bowling: float, fielding: float, 
                 wicket_keeping: float, running: float, experience: float, 
                 overs_bowled: int = 0, is_out: bool = False):
        
        self.name = name
        self.batting = batting
        self.bowling = bowling
        self.fielding = fielding
        self.wicket_keeping = wicket_keeping
        self.running = running
        self.experience = experience
        self.overs_bowled = overs_bowled
        self.is_out = is_out

        self.batting_criteria = round((self.batting + self.running + self.experience) / 3, 2)
        self.bowling_criteria = round((self.bowling + self.experience) / 2, 2)