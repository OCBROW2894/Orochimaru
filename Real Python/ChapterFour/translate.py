'''
* Challenge : Turn Your User Into a L33t H4x0r

Write a script called translate.py that asks the user for some input
 with the following prompt: Enter some text:. Then use the .replace()
 method to convert the text entered by the user into“leetspeak”by making
 the following changes to lower-case letters:
 • Theletter a becomes 4
 • Theletter b becomes 8
 • Theletter e becomes 3
 • Theletter l becomes 1
 • Theletter o becomes 0
 • Theletter s becomes 5
 • Theletter t becomes 7
 Your program should then display the resulting string as output. Be
low is a sample run of the program:
 Enter some text: I like to eat eggs and spam.
 I 1ik3 70 347 3gg5 4nd 5p4m.
'''
text=input("Enter some text: ")
leetspeak=text.replace("a","4")
leetspeak=leetspeak.replace("b","8")
leetspeak=leetspeak.replace("e","3")
leetspeak=leetspeak.replace("l","1")
leetspeak=leetspeak.replace("o","0")
leetspeak=leetspeak.replace("s","5")
leetspeak=leetspeak.replace("t","7")
print(leetspeak)
