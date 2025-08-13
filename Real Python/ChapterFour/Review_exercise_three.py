'''Question 1 : Writeascriptthatconvertsthefollowingstringstolowercase: "An
imals", "Badger", "Honey Bee", "Honeybadger". Print each lowercase
 string on a separate line. '''
name_one="Animals".lower()
name_two="Badger".lower()
name_three="Honey Bee".lower()
name_four="Honeybadger".lower()
print(name_one)
print(name_two)
print(name_three)
print(name_four)

''' Qustion 2 : Repeat Exercise 1, but convert each string to uppercase instead of
 lowercase. '''
name_one="Animals".upper()
name_two="Badger".upper()
name_three="Honey Bee".upper()
name_four="Honeybadger".upper()
print(name_one)
print(name_two)
print(name_three)
print(name_four)

'''Question 3 : Write ascript that removes whitespace from the following strings:
 string1 = "    Filet Mignon"
 string2 = "Brisket    "
 string3 = " Cheeseburger    "
 Print out the strings with the whitespace removed. '''
string1="    Filet Mignon".lstrip()
string2="Brisket    ".rstrip()
string3="  Cheeseburger  ".strip()
print(string1)
print(string2)
print(string3)

'''Question 4 : Writeascriptthatprintsouttheresultof.startswith("be")oneach
 of the following strings:
 string1 = "Becomes"
 string2 = "becomes"
 string3 = "BEAR"
 string4 = "  bEautiful"
 '''
string1 ="Becomes"
string2="becomes"
string3="BEAR"
string4="  bEautiful"
string1=string1.startswith("be")
string2=string2.startswith("be")
string3=string3.startswith("be")
string4=string4.startswith("be")
print(string1)
print(string2)
print(string3)
print(string4)
