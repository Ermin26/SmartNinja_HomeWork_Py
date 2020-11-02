
import time

print("                                 Hello there.")

time.sleep(1)

print("Please enter the number and program will count to that number. Numbers divisible  by 3 will write fizz, for numbers divisible by 5 will write buzz.")
time.sleep(5)
print("What will write for numbers divisible by 3 and 5?? Try and see.")
time.sleep(5)

print("Let's start. Please Enter one number bellow.")
time.sleep(2)
num = int(input("Your number:"))


for fizzbuzz in range(num):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

