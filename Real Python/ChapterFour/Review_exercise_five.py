''' Question 1 : Create a string containing an integer, then convert that string into
 an actual integer object using int(). Test that your new object is a number by multiplying
 it by another number and displaying the result. '''

##eggs=input("Enter the number of eggs you want to buy: ")
##price=18
##
##no_eggs=int(eggs)
##total_cost=no_eggs*price
##print(total_cost)

'''Question 2 : Repeatthepreviousexercise, but use a floating-point number and float(). '''
##eggs=input("Enter the number of eggs you want to buy: ")
##price=18.00
##
##no_eggs=float(eggs)
##total_cost=no_eggs*price
##print(total_cost)

'''Question 3 : Createastringobjectandanintegerobject,thendisplaythemside
by-side with a single print statement by using the str() function. '''
##boo_age=20
##bum_age="24"
##difference=int(bum_age)-boo_age
##print("My Boo is "+ str(difference) +" years younger than me, she's "+ str(boo_age)+ " and I'm "+bum_age)

'''Question 4 : Write a script that gets two numbers from the user using the
 input() function twice, multiplies the numbers together, and displays the result.
 If the user enters 2 and 4, your program should print the following text:
 The product of 2 and 4 is 8.0. '''

num_one=int(input("Please enter the first Number: "))
num_two=int(input("Please enter the second Number: "))
result=float(num_one*num_two)
print("The product of "+str(num_one)+ " and "+ str(num_two)+ " is "+ str(result)+".")
##print("The product of ", str(num_one), " and ", str(num_two), " is ", str(result),".")
