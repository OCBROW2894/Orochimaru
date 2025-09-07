"""
 Question : Write a script that prompts the user to enter a word using the
 input() function, stores that input in a variable, and then displays
 whether the length of that string is less than 5 characters, greater
 than 5 characters, or equal to 5 characters by using a set of if, elif and else statements.
"""

word = input("Enter a word to get it's length: ")
length = len(word)

if length > 5 :
    print(f"{word} has more than 5 characters, {length} to be exact")

elif length == 5 :
    print(f"{word} has 5 characters")

else :
    print(f"{word} has less than 5 characters, {length} to be exact")
