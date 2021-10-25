# paste in your finished solution for "calling functions activity"
# remove your function calls and instead create a menu running in a while loop
# give the option for the user to call the all your homies except homie_3

def homie_1():
    print("I got you my guy")


def homie_2():
    print("drive safe now and always")


def drake():
    print("I know when that hotline bling")


def homie_3(payment_to_homie):
    money_owed_to_homie_3 = 50
    money_owed_to_homie_3 -= payment_to_homie
    homie_3s_response = ""

    if money_owed_to_homie_3 > 0:
        homie_3s_response = "WHERES MY MONEY AT!?"
    elif money_owed_to_homie_3 == 0:
        homie_3s_response = "whatchu want this time!? I'm still mad"
    elif money_owed_to_homie_3 < 0:
        homie_3s_response = "hello my good friend, lets goooo"

    return homie_3s_response


def call_everyone(payment_to_homie):
    homie_1()
    homie_2()
    drake()
    print(homie_3(payment_to_homie))


while True:
    user_answer = input(
        "Which homie would you like to call? (options: homie_1, homie_2, homie_3, drake or q if you want to end this programme): ")
    if user_answer == "homie_1":
        homie_1()
    elif user_answer == "homie_2":
        homie_2()
    elif user_answer == "drake":
        drake()
    elif user_answer == "homie_3":
        payment = int(input("How much would you like to pay back? "))
        try:
            print(homie_3(payment))
        except ValueError:
            print("Invalied input")
    elif user_answer == "q":
        break
    else:
        print("Sorry, that's not in options")

# HARD MODE CHALLENGE
# create an option that when inputed allows the user to enter an amount paid and call homie_3
