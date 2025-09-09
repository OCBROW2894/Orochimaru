"""Question 1 : Write a script that repeatedly asks the user to input an integer,
 displaying a message to “try again” by catching the ValueError that
 is raised if the user did not enter an integer.
 
 Once the user enters an integer, the program should display
 the number back to the user and end without crashing.
"""

##while True :
##    try:
##        num = int(input("Enter an Integer: "))
##        print(f"{num}")
##        break
##    except ValueError:
##        print("Try Again! Integer please.")

"""Question 2 : Writeaprogramthataskstheusertoinputastringandaninteger
 n. Then display the character at index n in the string.
 
 Use error handling to make sure the program doesn’t crash
 if the user does not enter an integer or the index is out of bounds.
 The program should display a different message depending on
 what error occurs.
"""
s = input("Enter a string: ")

while True:
    try:
        n = int(input("Enter an integer: "))
        
        answer = s[n]
        
        print(f"{answer}")
        break
    except ValueError:
        print("That is not an integer!")
        
    except:
        print("The is larger than the length of the string you provided!")
