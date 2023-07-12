import sys
sys.path.append("..")
from cruv.player import Player
from typing import List
import numpy as np

def batsman_prob(batting_criteria: float) -> List[float]:
    probabilities = []
    sum_total = 0
    prob_total = 0
    smallest_probability = 1
    smallest_probability_index = -1

    # 0.83 -> [1, 2, 3, 4, 5, 6] - sum = 1
    # 1 -> 6 unique numbers that sum up to it
    for i in range(6):
        probabilities.append(np.random.randint(1, 6))
        sum_total += probabilities[i]
    
    for i in range(len(probabilities)):
        # runs are based on the batting criteria
        # index 0 - 3 & index 5 refer to one, two,three, four, and six
        # since arrays are 0-indexed it might take a while to pick this up
        # refer to batsman_schema in 'globals.py' in the parent directory
        if(i < 3 or i == 5):
            probabilities[i] = round(
                (probabilities[i]) / sum_total, 2)
        # getting out is based on 1 - batting criteria (i.e. it's compliment)
        # index 4 refers to out
        else:
            probabilities[i] = round(
                (probabilities[i]) / sum_total, 2)
        
        if(probabilities[i] != 0 and probabilities[i] < smallest_probability):
            smallest_probability_index = i
        prob_total += probabilities[i]
    
    if(prob_total != 1):
        diff_in_probability = 1 - prob_total
        prob_total += diff_in_probability
        probabilities[smallest_probability_index] += diff_in_probability
        probabilities[smallest_probability_index] = round(
            probabilities[smallest_probability_index], 2)

    return probabilities

# similarly we calculate bowler probabilities
def bowler_prob(bowling_criteria: float) -> List[float]:
    probabilities = []
    sum_total = 0
    prob_total = 0

    smallest_probability = 1
    smallest_probability_index = -1

    for i in range(4):
        probabilities.append(np.random.randint(1, 5))
        sum_total += probabilities[i]

    for i in range(4):
        if i == 0:
            probabilities[i] = round(
                (probabilities[i]) / sum_total, 2)
        else:
            probabilities[i] = round(
                (probabilities[i]) / sum_total, 2)        
        
        if(probabilities[i] != 0 and probabilities[i] < smallest_probability):
            smallest_probability = probabilities[i]
            smallest_probability_index = i
        
        prob_total += probabilities[i]
    
    if(prob_total != 1):
        diff_in_probability = 1 - prob_total
        probabilities[smallest_probability_index] += diff_in_probability
        probabilities[smallest_probability_index] = round(
            probabilities[smallest_probability_index], 2)
        
    return probabilities

# player = Player("Robert Collins",0.85,0.87,0.92,0.89,0.73,0.92)

# opt = batsman_prob(player.batting_criteria)
# print(opt, sum(opt))