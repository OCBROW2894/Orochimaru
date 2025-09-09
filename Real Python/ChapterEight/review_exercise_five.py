"""Question 1 : Write a script that repeatedly asks the user to input an integer,
 displaying a message to “try again” by catching the ValueError that
 is raised if the user did not enter an integer.
 
 Once the user enters an integer, the program should display
 the number back to the user and end without crashing.
"""

while True :
    try:
        num = int(input("Enter an Integer: "))
        print(f"{num}")
        break
    except ValueError:
        print("Try Again! Integer please.")

