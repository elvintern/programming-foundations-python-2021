# Demonstration of functions

import random

# ***********************
# These are functions - they only execute when called
# ***********************


def magic_8_ball():
    """ This function prints a response at random"""

    response = random.randint(1, 6)

    if response == 1:
        print("It is certainly so!")
    elif response == 2:
        print("No way")
    elif response == 3:
        print("Not at this time")
    else:
        print("I don't know... ask again")


def feedback(level):
    """ This function gives feedback based on the level"""
    """ This function has one parameter """

    if level < 5:
        print("Hmm... do you need some help?")
    elif level > 5 and level <= 15:
        print("Yay! That's a good start, keep going!")
    else:
        print("You're going great guns!")

# ***********************
# The main body of code starts here
# ***********************


magic_8_ball()
print("This is the beginning of the program")
feedback(5)
feedback(6)
feedback(20)
