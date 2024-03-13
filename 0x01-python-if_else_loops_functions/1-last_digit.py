#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = int(str(number)[-1]) * (-1 if number < 0 else 1)
text = ""

if number > 5:
    text = "and is greater than 5"
elif number == 0:
    text = "and is 0"
elif number < 6 and last_digit != 0:
    text = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {text:s}")
