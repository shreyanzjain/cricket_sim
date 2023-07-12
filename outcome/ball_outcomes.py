import numpy as np
from globals import BATTING_CHOICES, BOWLING_CHOICES
from player import Player

def batsman_outcome(player: Player) -> int:
    batting_chc = np.random.choice(BATTING_CHOICES, p=BATTING_PROBABILITIES)
    return 0

def bowler_outcome(player: Player) -> int:
    bowling_chc = np.random.choice(BOWLING_CHOICES, p=BOWLING_PROBABILITIES)
    return 0