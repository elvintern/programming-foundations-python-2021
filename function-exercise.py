# Function exercises that take no, one or two parameters

# Exercise 1
# Add a line of code that calls the function made_me() so the following is output:
# "You made me print this"
# Add more lines of code to call the function made_me() two more times

def made_me():
    """ This function prints a message to the screen """
    for i in range(1, 3):
        print("You made me print this")


made_me()


# Exercise 2
# Add a line of code that calls the function display() so the following is output:
# "Ahoy there, I have a message for you"
# "Would you like a game of tennis?"
# Play with printing out other messages

def display(message):
    """ This function prints a message to the screen """
    print("Ahoy there, I have a message for you")
    print(message)


display("Would you like a game of tennis?")
display("I want KFC right now")

# Exercise 3
# Write your own function called shouting(message)
# Your function should have one parameter called message and print the message in capital letters
# There is a string method you can use for this - look it up on w3school
# Call your function three times with different messages


def shouting(message):
    print(message.upper())


shouting("i am hungry")
shouting("i said i want kfc")
shouting("right now!!")


# Exercise 4
# Write a function called format_msg(message, person).
# Your function should create a concatonated message and print to the screen. Eg if given the data
# "Good morning" and "Brendan" print the output "$$$$ Good morning Brendan! $$$$"

def format_msg(message, person):
    print("$$$$ " + message + " " + person + " $$$$")


format_msg("Hi", "KFC")
