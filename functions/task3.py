"""
You are going to create a 
number-guessing game. In this game, 
the player has 5 valid attempts to 
guess a secret number between 1 and 10. You need to implement a function that handles the following game logic:
The secret number is stored in a 
global variable ( you decide what it 
will be ).
The player's guess will be stored in 
a local variable.
If the guess is out of bounds 
(less than 1 or greater than 10), 
it should be ignored (ex.: do nothing 
and continue the game, but don't 
count this as a valid attempt).
If the player guesses the correct 
number, the game should immediately 
end, and the function should print a 
congratulatory message.
The game ends after the player either 
guesses the correct number or uses 
up all 5 valid attempts. Write a 
function guess_game() that will 
implement the above logic and manage 
the player's attempts. Use the break,
continue or pass statements if and 
where appropriate.
"""

import random

# Global variable to store the secret number
secret_number = random.randint(1, 10)

def guess_game():
    attempts = 5  # Number of valid attempts

    print("Welcome to the number-guessing game!")
    print("Guess a number between 1 and 10.")

    while attempts > 0:
        # Ask the player for a guess
        guess = input("Enter your guess: ")

        # Check if the input is a valid integer
        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        # Convert the valid input to an integer
        guess = int(guess)

        # Check if the guess is out of bounds
        if guess < 1 or guess > 10:
            print("Your guess is out of bounds. Please guess a number between 1 and 10.")
            continue  # Ignore this guess and let the player try again

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number: {secret_number}")
            break  # End the game immediately if the guess is correct

        # If the guess is incorrect
        print("Wrong guess! Try again.")
        attempts -= 1  # Decrease the number of valid attempts

        # Display remaining attempts
        if attempts > 0:
            print(f"You have {attempts} attempts left.")
        else:
            print(f"Game over! The correct number was: {secret_number}")

# Call the game function
guess_game()
