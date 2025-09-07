"""
* Killing Bugs using the debugger
"""

def add_underscores(word):
    new_word = "_"
    for char in word:
        new_word = new_word + char + "_"
    return new_word

phrase = "hello"
print(add_underscores(phrase))
