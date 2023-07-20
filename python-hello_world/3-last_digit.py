#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#  we get the last digit of the number using modulo operator
last_digit = abs(number) % 10

# we Check the conditions and print the output accordingly
if number < 0:
    last_digit *= -1  # If the number is negative, we make the last digit negative as well

print("The string Last digit of", number, "is", last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
