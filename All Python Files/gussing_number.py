from random import randint



name = input("What is your name?: ")
print(f"Welcome to the guessing game {name}!")
print("I am thinking of a number between 1 and 100.")

# Set a random secret number between 1 and 100 for the player to guess
secret_key = randint(1, 100)

# Define constants for the number of attempts in each difficulty level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to let player choose difficulty and return number of attempts
def set_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input, defaulting to easy")
        return EASY_LEVEL_TURNS

# Set the initial number of attempts based on player's difficulty choice
attempts = set_level()

# Function to get a guess from the player with error handling
def make_guess():
    try:
        guess = int(input("Enter a number between 1 and 100: "))
        return guess
    except ValueError:
        print("Please enter a number!") 
        return -1

# Initialize counter to track how many guesses the player takes
guesses_taken = 0

# Main game loop: runs while player has attempts left
while attempts > 0:
    attempts = attempts -1 # Decrease remaining attempts by 1
    guesses_taken = guesses_taken + 1 # Increase guess counter by 1

    guess_2 = make_guess()
    if guess_2 > secret_key:
        print(f"Too high, you have {attempts} guesses left. Try again!!")
    elif guess_2 < secret_key:
        print(f"Too low, you have {attempts} guesses left. Try again!!")

    else:
        print(f"You got it, {name}! It took you {guesses_taken} guesses!")
        break # Exit loop when player guesses correctly

# Check if player ran out of attempts and display game over message
if attempts == 0:
    print("Game over, you are out of guesses!")
                  