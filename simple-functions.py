# Modify the below code so that the printing for credits is placed into a function
# the printing of the numbers from 1-20 is placed into a function

# these functions can be called and run from the menu while loop


# put credits code into a function
def credits(person_name):
    print("program by", person_name)
    print("lighting by a torch")
    print("facility by unitec")


# put number printer code into a function

def num_printer():
    for number in range(1, 21):
        print(number)


while True:
    choice = input(
        "enter c to see credits, n to see every number from 1-20, q to quit ")
    if choice == "c":
        credits("Jinwoo Park")
    elif choice == "n":
        num_printer()
    elif choice == "q":
        break

print("laters g")
