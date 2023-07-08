from abc import ABC, abstractmethod

class ITeam(ABC):
    
    @abstractmethod
    def generate_batting_order():
        pass
    
    @abstractmethod
    def generate_bowling_order():
        pass

    @abstractmethod
    def select_captain():
        pass

    @abstractmethod
    def send_player():
        pass

    @abstractmethod
    def choose_bowler():
        pass