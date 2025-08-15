''' Question 1 : Create a string containing an integer, then convert that string into
 an actual integer object using int(). Test that your new object is a number by multiplying
 it by another number and displaying the result. '''

eggs=input("Enter the number of eggs you want to buy: ")
price=18

no_eggs=int(eggs)
total_cost=no_eggs*price
print(total_cost)
