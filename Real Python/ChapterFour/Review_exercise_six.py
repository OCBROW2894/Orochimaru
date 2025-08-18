'''Question 1 : Create a float object named weight with the value 0.2, and create
 a string object named animal with the value "newt". Then use these
 objects to print the following string using only string concatenation:
 0.2 kg is the weight of the newt. '''

##weight=float(0.2)
##animal= "newt"
##print(str(0.2)+ " kg is the weight of the " + animal + ".")

'''Question 2 : Display the same string by using the .format() method and empty
 {} place-holders.'''
weight=0.2
animal="newt"
print("{} kg is the weight of the {}.".format(weight,animal))
