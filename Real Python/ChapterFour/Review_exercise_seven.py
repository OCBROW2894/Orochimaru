'''
select the code you want to uncomment then press:
 Alt+4

'''

'''Question 1 : In one line of code, display the result of trying to .find() the sub-
string "a" in the string "AAA". The result should be-1.'''
##print("AAA".find("a"))

'''Question 2 : Replaceeveryoccurrenceofthecharacter"s"with"x"inthestring
 "Somebody said something to Samantha.". '''
##message= "Somebody said something to Samantha."
##message=message.replace("s","x")
##print(message)

'''Question 3 : Write and test a script that accepts user input using the input()
 function and displays the result of trying to .find() a particular letter in that input. '''
test=input("What was the name of the Fourth Hokage and what was his nickname: ")
search=test.find("Yellow Flash")
print(search)
