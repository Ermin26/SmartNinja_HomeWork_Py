
while True:

    choose = input("""
        Choose a for x + y
        Choose b for x - y
        Choose c for x * y
        Choose d for x / y
        Choose e for x ** y
        Choose f for cancel
            Your choice:""")

    if choose == "a":
        x = int(input("Please enter first number: "))
        y = int(input("Please enter first number: "))
        print(x + y)

    elif choose == "b":
        x = int(input("Please enter first number: "))
        y = int(input("Please enter first number: "))
        print(x - y)

    elif choose == "c":
        x = int(input("Please enter first number: "))
        y = int(input("Please enter first number: "))
        print(x * y)

    elif choose == "d":
        x = int(input("Please enter first number: "))
        y = int(input("Please enter first number: "))
        print(x / y)

    elif choose == "e":
        x = int(input("Please enter first number: "))
        y = int(input("Please enter first number: "))
        print(x ** y)

    elif choose == "f":
        exit("Thank you for using calculator. Have nice day.")
    else:
        print("Sory, the calculator doesn't suport that!")

input("Pres Enter to restart calculator")
