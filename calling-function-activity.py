# call your homies

# follow the instructions on line 31 to call all these functions
# take note that homie_3() does not have a print statement built in and instead uses a return

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


call_everyone(100)

# write some function calls below to call all your homies and drake
# call homie_3 within a print statement to get a printed response
# make sure you pay them back enough money to get a positive response this time
