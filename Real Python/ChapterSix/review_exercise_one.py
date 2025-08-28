"""Question 1 : Write a function called cube() with one number parameter and re
turns the value of that number raised to the third power. Test the
 function by displaying the result of calling your cube() function on
 a few different numbers. """

def cube(x):
    """Raises the number x to the third power"""
    sol = pow(x,3)
    return sol

base = float(input("Enter a number: "))

answer = cube(base)
print(f"{base} cubed is {answer}.")

