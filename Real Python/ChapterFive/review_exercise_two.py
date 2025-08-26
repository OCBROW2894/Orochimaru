'''Question 1 : Write a script that asks the user to input a number and then dis
 plays that number rounded to two decimal places. When run,your
 program should look like this:
 Enter a number: 5.432
 5.432 rounded to 2 decimal places is 5.43
 '''
##n = float(input("Enter a number: "))
##
##rounded_n = round(n,2)
##
##print(f"{n} rounded to 2 decimal places is {rounded_n}")

'''Question 2 : Write a script that asks the user to input a number and then dis
 plays the absolute value of that number. When run, your program
 should look like this:
 Enter a number:-10
 The absolute value of-10 is 10.0
 '''
##n = float(input("Enter a number: "))
##absolute_n = abs(n)
##
##print(f"The absolute value of {n} is {absolute_n}")

'''Question 3 : Write a script that asks the user to input two numbers by using the
 input() function twice, then display whether or not the difference
 between those two number is an integer. When run,your program
 should look like this:
 Enter a number: 1.5
 Enter another number: .5
 The difference between 1.5 and .5 is an integer? True!
 If the user inputs two numbers whose difference is not integral,
 the output should look like this:
 Enter a number: 1.5
 Enter another number: 1.0
 The difference between 1.5 and 1.0 is an integer? False!
 '''
n = float(input("Enter a number: "))
m = float(input("Enter another number: "))
answer = (n-m).is_integer()
print(f"The difference between {n} and {m} is an integer? {answer}!")
