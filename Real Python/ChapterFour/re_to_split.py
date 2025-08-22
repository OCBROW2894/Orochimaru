'''
* Use re.split() for Advanced String Splitting
 Here’s a list of the regex constructs that you used to make this split happen:

\s: Matches any whitespace character.
*: Matches zero or more occurrences of the preceding.
(?:): Creates an alternation group, for example (?:abc|def), that matches any of the patterns abc or def in their entirety. In your specific example, this allows you to treat AND as a single delimiter to split on.
[]: Creates a character set that matches any one of the characters inside the square brackets.
+: Matches one or more occurrences of the preceding.



'''
###NOTE:This Code only works in the interactive screen
##import re
##
##shopping_list = "Apple  :::::3:Orange  |  2|||Lemon --1 AND Date :: 10"
##pattern = r"\s*(?:[:|\-]+|AND)\s*"
##
##re.split(pattern, shopping_list)
import re

shopping_list = "Apple:Orange|Lemon-Date"
actual_list=re.split(r"[:|-]",shopping_list)
print(actual_list)
