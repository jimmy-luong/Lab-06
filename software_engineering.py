# Jimmy Luong


def encode(string):
    password = ""
    for i in string:  # reads through the string and adds 3 to each number
        val = int(i) + 3
        if val >= 10:
            val -= 10
        password += str(val)
    return password


def decode(string):
    password = ''
    for i in string:
        val = int(i) - 3
        if val < 0:
            val += 10
        password += str(val)
    return password


while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")

    option = int(input("Please enter an option: "))

    if option == 1:  # option to call the encoder function
        code = input("Please enter your password to encode: ")
        code = encode(code)
        print("Your password has been encoded and stored!")
        print("")
    if option == 2:
        print(f'The encoded password is {code}, and the original password is {decode(code)}.')
        print()
    elif option == 3:
        break

