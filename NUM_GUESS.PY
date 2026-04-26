"""
Number Guessing Game 🎯
Author: Your Name
Description: A simple CLI game where the user guesses a randomly generated number.
"""

import random

print("🎯 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")

# Generate random number
secret_number = random.randint(1, 100)

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low! Try again.")
        elif guess > secret_number:
            print("Too High! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number!")
