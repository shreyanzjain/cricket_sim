from player import Player
from typing import List
import numpy as np

def batsman_prob(player: Player) -> List[float]:
    probabilities = []
    sum_total = 0
    prob_total = 0
    smallest_probability = 1
    smallest_probability_index = -1

    # 0.83 -> [1, 2, 3, 4, 5, 6] - sum = 1
    # 1 -> 6 unique numbers that sum up to it
    for i in range(6):
        probabilities.append(np.random.randint(0, 5))
        sum_total += probabilities[i]
    
    for i in range(len(probabilities)):
        # runs are based on the batting criteria
        # index 0 - 3 & index 5 refer to one, two,three, four, and six
        # since arrays are 0-indexed it might take a while to pick this up
        # refer to batsman_schema in globals.py in the parent directory
        if(i < 3 or i == 5):
            probabilities[i] = round(
                (player.batting_criteria * probabilities[i]) / sum_total, 2)
        # getting out is based on 1 - batting criteria (i.e. it's compliment)
        # index 4 refers to out
        else:
            probabilities[i] = round(
                ((1 - player.batting_criteria) * probabilities[i]) / sum_total, 2)
        
        if(probabilities[i] != 0 and probabilities[i] < smallest_probability):
            smallest_probability_index = i
        prob_total += probabilities[i]
    
    if(prob_total != 1):
        diff_in_probability = 1 - prob_total
        prob_total += diff_in_probability
        probabilities[smallest_probability_index] += diff_in_probability
        probabilities[smallest_probability_index] = round(probabilities[smallest_probability_index], 2)

    print(probabilities, sum(probabilities))
    return probabilities