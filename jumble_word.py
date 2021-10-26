# Word jumble with functions

import random

################################
# Functions


def display_instructions():
    """ This function displays the instructions """
    print("Unscramble the letters to make a word")


def string_to_list(word_string):
    """ This function takes a string and returns a list of letters """
    output_list = []
    for string in word_string:
        output_list.append(string)
    return output_list


def list_to_string(word_list):
    """ This function takes a list of letters and returns a string """
    output_string = ""
    for i in word_list:
        output_string += i
    return output_string


def format_message(message):
    """ This function takes a string and formats it into an output message"""
    pass


def goodbye_message():
    """ This function displays the goodbye credits"""
    print("Thanks for playing")

################################
# Main body of code


def jumble_word():
    # sequence of words to choose from
    WORDS = ["jumble", "washing", "spatula", "answer", "zylophone"]
    shuffled_word_string = ""

    # Welcome message and instructions
    print("Hello, and welcome to word jumble \n")
    display_instructions()

    # choose a word at random from the list
    word_string = random.choice(WORDS)

    # turn word into a list  of letters
    word_list = string_to_list(word_string)

    # shuffle the letters in list
    random.shuffle(word_list)

    # convert shuffled letters to one string
    shuffled_word_string = list_to_string(word_list)

    # Print jumbled word to screen
    print("Here is your word:")
    print(shuffled_word_string)
    print("\n")

    # Loop waiting for correct guess or q to quit

    count = 0

    while True:
        guess = input("What is the word? (or q to quit)")
        count += 1
        if guess == word_string:
            print("\n******************************")
            print("Congratulations - that's correct!")
            print("You only guessed", count, "times!")
            print("******************************")
        elif guess == "q":
            # Print goodbye message
            goodbye_message()
            break
        else:
            print("Please try again")


jumble_word()
