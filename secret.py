# noinspection PyUnresolvedReferences
import random

import time

print("Hello there")
time.sleep(2)
print("Let's play a game :D")
time.sleep(2)

secret = random.randint(1, 60)
guess = None


number_of_tries = 5


for x in range(5):
    print(f"you have {number_of_tries} tries to get correct secret number.")
    time.sleep(1)
    try:
        guess = int(input("Guess the secret randomly chosen number between 1 and 60: "))
        time.sleep(0.500)
    except:

        print("Please input the number, letters not included!")
        continue

    number_of_tries -= 1

    if guess < secret:
        print("Litlle help for you. The secret number is bigger.")
        time.sleep(0.500)
    elif guess == secret:
        print(f"Congratulations. You've guessed it!:D The secret number is: {secret}")
        break
    else:
        print("Litlle help for you. The secret number is lower.")
        time.sleep(1)

print("Sorry. You didn't get it.")
time.sleep(0.300)
print(f"The secret number is {secret}")