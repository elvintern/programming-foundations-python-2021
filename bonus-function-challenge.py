string_1 = "pineapple"
print("string we messing with: ", string_1)

for letter in string_1:
    print("letter in our string: ", letter)
    if letter == "a":
        print("ouch, this loop just hit an a")
print("our string in uppercase: ", string_1.upper())

string_2 = "kendrick lamar"
print("string we messing with: ", string_2)

for letter in string_2:
    print("letter in our string: ", letter)
    if letter == "a":
        print("ouch, this loop just hit an a")
print("our string in uppercase: ", string_2.upper())


string_3 = "j cole"
print("string we messing with: ", string_3)

for letter in string_3:
    print("letter in our string: ", letter)
    if letter == "a":
        print("ouch, this loop just hit an a")
print("our string in uppercase: ", string_3.upper())

string_4 = "first things first rest in peace uncle Phill"
print("string we messing with: ", string_4)

for letter in string_4:
    print("letter in our string: ", letter)
    if letter == "a":
        print("ouch, this loop just hit an a")
print("our string in uppercase: ", string_4.upper())


def find_a():
    user_input = input("Input text that you want to find 'a'").lower()
    for letter in user_input:
        if letter == "a":
            print("ouch, this loop just hit an a")
        else:
            print("letter in our string: ", letter)
    print("our string in uppercase: ", user_input.upper())


find_a()
