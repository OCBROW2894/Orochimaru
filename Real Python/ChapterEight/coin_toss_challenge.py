"""
* Challenge: Simulate a CoinToss Experiment
"""

import random

def coin_toss():
    """Coin flip"""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

flips = 1
flips_per_trial = 0
outcome = coin_toss()

for trial in range(10_000 + 1):
    while outcome == coin_toss():
        flips = flips + 1
    else:
        flips_per_trial = flips
        new_f_p_t = flips_per_trial
        flips = flips + 1
        trial = trial + 1
        print(f"{flips_per_trial} {flips} {trial}")

    flips_per_trial = flips_per

        



        
