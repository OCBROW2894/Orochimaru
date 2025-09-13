"""
* Challenge: Simulate an Election
"""

import random

#Probabilities for Candidate A to win each region
region1_prob = 0.87
region2_prob = 0.65
region3_prob = 0.17

a_wins = 0

for trial in range(10_000):
    wins = 0

    #Simulating each region one by one
    if random.random() < region1_prob:
        wins += 1
    if random.random() < region2_prob:
        wins += 1
    if random.random() < region3_prob:
        wins += 1

    #Candidate A needs at least 2 regions to win
    if wins >= 2:
        a_wins += 1
        

#percentage of A wins
percentage = ( a_wins / 10_000 )* 100

print(f"Candidate A wins in {percentage:.2f}% of the simulation.")
    

        



        
