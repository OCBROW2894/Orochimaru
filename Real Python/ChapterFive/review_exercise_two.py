'''Question 1 : Write a script that asks the user to input a number and then dis
 plays that number rounded to two decimal places. When run,your
 program should look like this:
 Enter a number: 5.432
 5.432 rounded to 2 decimal places is 5.43
 '''
n = float(input("Enter a number: "))

rounded_n = round(n,2)

print(f"{n} rounded to 2 decimal places is {rounded_n}")
