# Function exercises that return a value

# Exercise 1
# Add a line of code to call give_me_fiveand print the return value

def give_me_five():
    five = 5
    return five


print(give_me_five())

# Exercise 2
# Add a line of code that calls give_me_five() and stores the return value in a variable


def give_me_five():
    five = "five"
    return five


print(give_me_five())

# Exercise 3
# Add some code so that give_me_five() is called in a loop that repeats 5 times


def give_me_five():
    count = 0
    while count < 5:
        five = "five"
        print(five)
        count += 1


give_me_five()


# Exercise 4
# Add some code that keeps a running total of the total of 5s
# By the end of 5 iterations of the loop the total should be 25

def give_me_five():
    count = 0
    total = 0
    while count < 5:
        five = 5
        count += 1
        total += 5
        print(five)
    print(total)


give_me_five()

# Exercise 5
# Call ask_yes_no with the question "Are you hungry?", and again with "Fancy a cheese sandwich?"


def ask_yes_no(question):
    response = ""
    while response not in ["y", "n"]:
        response = input(question)
    return response


ask_yes_no("Are you hungry?")
ask_yes_no("Fancy a cheese sandwich?")

# Exercise 6
# Add some if/else statements to your code above to give replies to the user based on their
# response. For example if they are hungry offer a cheese sandwich, if they aren't tell
# them to stop looking in the fridge.


def ask_yes_no(question):
    response = input(question)
    if response == "y":
        response = input("Fancy a cheese sandwich? ")
    elif response == "n":
        print("Then stop looking in the fridge!")
    else:
        print("Invalied Error")


ask_yes_no("Are you hungry?")
