#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0 :
    print(f"{number} is positive")
if number==0 :
    print(f"{number} is zero")
if number < 0 :
    print(f"{number} is negative")