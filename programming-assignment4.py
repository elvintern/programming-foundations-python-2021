# Hero's inventory
# Using list operations and methods

import random

inventory = ["sword", "armour", "shield", "healing potion"]
menu_options = """These are your options:
                   1 - show inventory
                   2 - add item to inventory
                   3 - number of items in inventory
                   4 - remove item from inventory
                   5 - swap item in inventory for a different item at position"""


def item_swap_function():
    while True:
        swap_item = input("Which item do you want to move?: ")
        if swap_item not in inventory:
            print("You don't have that item :(")
            break
        else:
            swap_item_with = input(
                "Which item do you want to swap with?: ")
            if swap_item_with not in inventory:
                print("You don't have that item :(")
                break
            elif swap_item_with in inventory:
                swap_item_index = inventory.index(swap_item)
                swap_item_with_index = inventory.index(
                    swap_item_with)
                inventory[swap_item_index], inventory[swap_item_with_index] = inventory[
                    swap_item_with_index], inventory[swap_item_index]
                print("Items have been swapped :)")
                break


def game_start():
    # Welcome message
    print("Welcome! I am here to help you manage your inventory")
    # Loop until player enters q to quit
    while True:
        user_input = str(input(
            "\nWhat would you like to do? Enger i to see the options, q to quit: "))
    # Code for option 'q'
        if user_input == "q":
            break
    # Code for option 'i'
        elif user_input == "i":
            print(menu_options)
    # Code for option '1'
        elif user_input == "1":
            print(inventory)
    # Code for option '2'
        elif user_input == "2":
            add_item = input("What would you like to add in your inventory?: ")
            inventory.append(add_item)
    # Code for option '3'
        elif user_input == "3":
            print("You have", inventory.__len__(), "items in your inventory")
            # Code for option '4'
        elif user_input == "4":
            remove_item = input(
                "What would you like to remove from your inventory?: ")
            if remove_item in inventory:
                inventory.remove(remove_item)
                print(remove_item, "has been removed :)")
            else:
                print("You don't have that item :(")
            # Code for option '5'
        elif user_input == "5":
            item_swap_function()
            # Goodbye message printed when exit the while loop
    print("Goodbye!")


game_start()
