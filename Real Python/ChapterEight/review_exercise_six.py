"""Question 1 : Write a function called roll() that uses the randint() function to
 simulate rolling a fair die by returning a random integer between
 1 and 6.
"""
##import random
##
##def roll():
##    n = random.randint(1,6)
##    print(n)
##    return n
##
##roll()

"""Question 2 : Write a script that simulates 10,000 rolls of a fair die and displays
 the average number rolled.
"""
import random

def roll():
    n = random.randint(1,6)
    return n

num_rolls = 10_000
total = 0

for trial in range(num_rolls):
    total = total + roll()

avg_roll = total / num_rolls

print(f"The average result of {num_rolls} rolls is {avg_roll:.3f}")
