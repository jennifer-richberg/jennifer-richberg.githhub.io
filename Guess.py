## This is the Guessing Number Game

import random

n = random.randint(1,99)

guess = int(input("Enter integer from 1 to 99: "))

while n != "guess":
    print
    if guess < n:
        print("Guess is low")
        guess = int(input("Enter integer from 1 to 99: "))
   
    elif guess > n:
        print("Guess is high")
        guess = int(input("Enter integer from 1 to 99: "))
    else:
        print("Correct")
        breaks
    print


