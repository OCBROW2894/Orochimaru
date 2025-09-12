"""
* Challenge: Simulate a CoinToss Experiment
"""

import random

def one_trial():
    """Number of flips per trial"""
    outcome = random.randint(0, 1)
    flips = 1

    while outcome == random.randint(0, 1):
        flips = flips + 1

    flips = flips + 1
    return flips


trials = 0

for trial in range(10_000):
    trials = trials + one_trial()
    average = trials/10_000

print(f"The average flips per Trial is: {average:.3f}")
    

        



        
