"""Question 1 : Write a function called roll() that uses the randint() function to
 simulate rolling a fair die by returning a random integer between
 1 and 6.
"""
import random

def roll():
    n = random.randint(1,6)
    print(n)
    return n

roll()

