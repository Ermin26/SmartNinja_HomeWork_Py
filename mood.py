
import time

print("Hello there.")
time.sleep(1)

mood = input("What is your mood today?\n")

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Life is short, take a deep breath.")
elif mood == "sad":
    print("Cheer up and go on!")
elif mood == "excited":
    print("Wow, tell us moreee..")
elif mood == "relaxed":
    print("Yeah be calm and enjoy.")
else:
    print("I don't recognize this mood")