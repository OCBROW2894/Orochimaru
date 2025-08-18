###String interpolation
##n = int(3)
##m = int(4)
##s = n*m
##print(str(n) +" times "+ str(m) + " is " + str(n*m))
##print(str(n), " times ", str(m) , " is " , str(n*m))

n = 3
m = 4
print(f"{n} times {m} is {n*m}") #f-strings are only available in Python version 3.6 and above.
print("{} times {} is {}".format(n,m,n*m))#For earlier versions
