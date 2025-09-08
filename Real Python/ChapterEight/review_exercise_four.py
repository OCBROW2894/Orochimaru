"""Question 1 : Usingbreak,writeaprogramthatrepeatedlyaskstheuserforsome
 input and only quits if the user enters "q" or "Q".
"""

letter = input("Guess the special letter: ").lower()

while letter != "q" :
    letter = input("wrong! Guess again: ").lower()

    if letter == "q" :
        print(f"Congratulations! {letter} is the Special letter.")
        break
