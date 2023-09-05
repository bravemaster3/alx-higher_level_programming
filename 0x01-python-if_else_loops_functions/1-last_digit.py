#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if last_digit > 5:
    suffix = "is greater than 5"
elif last_digit > 0:
    suffix = "is less than 6 and not 0"
else:
    suffix = "is 0"
print(f'Last digit of number {number:d} is {last_digit:d} and {suffix}')
