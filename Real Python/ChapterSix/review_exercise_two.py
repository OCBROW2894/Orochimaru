"""Question 1 : Write a for loop that prints out the integers 2 through 10, each on
 a newline, by using the range() function. """
##for n in range(2,11):
##    print(n)

"""Question 2 : Use a while loop that prints out the integers 2 through 10 (Hint:
 You’ll need to create a new integer first.)"""

##n = 2
##
##while n <= 10:
##    print(n)
##    n = n + 1

"""Question 3 : Writeafunctioncalleddoubles()thattakesonenumberasitsinput
 and doubles that number. Then use the doubles() function in a
 loop to double the number2threetimes, displaying each result on
 a separate line. Here is some sample output:
 4
 8
 16
 """

def doubles(x):
    """Doubles the number x """
    doubled_x = x * 2
    return doubled_x


n = 2
times = 0

while times < 3 :
    n = doubles(n)
    print(n)
    times= times + 1

