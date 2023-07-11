#!/usr/bin/python3
def fizzbuzz():
    multiple_of_three = (num % 3) == 0
    multiple_of_five = (num % 5) == 0
    multiple_of_both = (num % 15) == 0
    for num in range(1, 101):
        if multiple_of_three:
            print("Fizz", end=" ")
        elif multiple_of_five:
            print("Buzz", end=" ")
        elif multiple_of_both:
            print("FizzBuzz", end=" ")
        else:
            print(f"{num}", end=" ")
