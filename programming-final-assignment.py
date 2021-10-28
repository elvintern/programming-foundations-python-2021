# RPG game element

import time
import random
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

greetings = ["Hi...(Awkwardly)", "Hey...(Awkwardly)",
             "(Ignoring...)", "(Giving you evil eyes)"]
leaving = ["Hey! Why are you running away? Hey!",
           "(ignoring...)", "Go to hell!", "Arggggh!"]
user_pocket = ["$5", "Lottery Ticket", "KitKat", "Couple Ring"]
ex_pocket = ["KFC Wicked Wings 20pk",
             "just normal pen", "diamond", "Couple Ring"]

# Function to format text and output to the screen

def speak(saying):
    print(Fore.BLUE + saying)

def ex_speak(ex_saying):
    print(Fore.RED + "\n\t\t\t\t\t" + ex_saying)

# Set the scene

def start():
    print("There is your ex-girlfriend coming down the road...")
    # Menu loop
    while True:
        # Get menu choice
        time.sleep(2)
        user_answer = input(
            "\nWhat would you like to do? 1 to greet, 2 play a game for fun, 3 play a game of chance, 4 run away: ")
        # Menu option 1 code (greeting)
        if user_answer == "1":
            user_greeting = input("Type in your greeting\n")
            time.sleep(2)
            ex_speak(random.choice(greetings))
        # Menu option 2 code (game for fun)
        elif user_answer == "2":
            speak("Do you want to play a game for fun?")
            time.sleep(2)
            ex_speak("Why do I have to play a game with you?")
            time.sleep(2)
            user_explain = input("Type in your answer\n")
            time.sleep(1.5)
            ex_speak("Bullshit!\n")
        # Menu option 3 code (game of chance)
        elif user_answer == "3":
            speak("Do you want to play a game of chance?")
            time.sleep(2)
            global ex_bet
            ex_bet = random.choice(ex_pocket)
            ex_speak("I would love to take away your items")
            time.sleep(2)
            ex_speak("I have a " + ex_bet + " that we can play for.")
            time.sleep(2)
            ex_speak("What would you like to bet?\n")
            time.sleep(2)
            print("These are in your pocket", user_pocket)
            global user_bet
            user_bet = input("Enter the item you will wager: ")
            if user_bet not in user_pocket:
                time.sleep(1)
                ex_speak("You don't have that!")
            else:
                time.sleep(2)
                ex_speak("Ummm... that is acceptable, let's play")
                time.sleep(2)
                ex_speak("************************************************")
                guess_my_number()

        # Menu option 4 code (Running away)
        elif user_answer == "4":
            user_leaving = input(
                "What would you like to say on running away?\n")
            time.sleep(2)
            ex_speak(random.choice(leaving))
            break

        # Invalid input message
        else:
            print("That's not an option bro")

# Function for game play
def guess_my_number():
    # Welcome the player and give the rules
    ex_speak("I've thought of a number between 1 and 100, you have 7 trys to guess it")
    time.sleep(2)
    ex_speak("If you guess correctly you will win my " + ex_bet)
    # Generate a secret number
    secret_num = random.randint(1, 100)
    correct_guess_b = False
    number_trys = 0

    # loop while the number hasn't been guessed correctly
    while correct_guess_b == False:
        # get a guess from the player
        time.sleep(1)

        # check the guess and give some feedback (Higher, lower, you win)
        try:
            guess = int(input("Make your guess\n"))
            number_trys += 1
            if secret_num == guess:
                time.sleep(1)
                print("Darn it!!!... you win in...", number_trys, "guesses")
                user_pocket.append(ex_bet)
                print("\nThe", ex_bet, "has been added to your pocket")
                time.sleep(2)
                print("These are in your pocekt", user_pocket)
                time.sleep(2)
                print("\nArggh! I shoudn't have played with you!!")
                correct_guess_b = True
            elif number_trys > 7:
                time.sleep(1)
                print("Hahahaha you are a loser!! The correct number is '{}'.".format(secret_num), "I will take your '{}'".format(user_bet))
                user_pocket.remove(user_bet)
                time.sleep(2)
                print("\nThe",user_bet,"has gone from your pocket")
                time.sleep(2)
                print("These are in your pocekt now",user_pocket)
                break
            elif secret_num > guess:
                print("Higher!")
            elif secret_num < guess:
                print("Lower!")
            else:
                print("Type in your Guess!")
            
        except:
            print("That's not a number!")
                
start()
