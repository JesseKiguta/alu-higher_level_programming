#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (abs(number) % 10) * (-1 if number < 0 else 1)
gt5 = "and is greater than 5"
zero = "and is zero"
lt6notzero = "and is less than 6 and not 0"
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} {gt5}")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} {zero}")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} {lt6notzero}")
