# write a program that will:

# ask for the user to enter their hight in CMs and convert it to an int

# if they are < 140cm reject them from the ride

customer_height_list = []

while True:

    user_input = input("Enter your height: ")
    if user_input == "q":
        print("heights going on the ride:", customer_height_list)
        print("bye have a nice day")
        break
    else:
        try:
            user_height = int(user_input)
            if user_height < 140:
                print("Sorry, you are too short")
                # if they are between 140 and 159 tell them "ok you can go on the ride"
            elif user_height >= 140 and user_height < 160:
                customer_height_list.append(user_height)
                print("ok you can go on the ride")
            # if they are between 160 and 179 tell them "you can go on the ride but watch out for dat tree"
            elif user_height >= 160 and user_height < 180:
                customer_height_list.append(user_height)
                print("you can go on the ride but watch out for dat tree")
            # if they are 180 or over tell them "sorry bro you are a giraffe"
            else:
                print("sorry bro you are a giraffe")
        except ValueError:
            print("Please enter your height in cm")
