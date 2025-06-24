# Day 3 - Number Guessing Game

import random

# Generate random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Compare
if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
else:
    print("You guessed it right!")

print("The correct number was:", secret_number)
