'''
* String Splitting
'''

##user_input=input("Please enter your FirstName LastName Age: ")
##user_data=user_input.strip().split()
####print(user_data)
##firstName, lastName, age =user_data
##print(f"Welcome {lastName} {firstName}! You're {age} years old.")


#Split With Different Delimiters Using sep
csv_line = "Ankita,Vishal,Jane,Naga,Emily,Maria"
csv_product_info = "Sweater,Blue,34.99,In Stock"
names=csv_line.split(sep=",")
fields=csv_product_info.split(",")
ex=names[2]
color=fields[1]

print(ex)
print(color)
 
