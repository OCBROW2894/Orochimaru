'''
* String Splitting
'''

user_input=input("Please enter your FirstName LastName Age: ")
user_data=user_input.strip().split()
##print(user_data)
firstName, lastName, age =user_data
print(f"Welcome {lastName} {firstName}! You're {age} years old.")
