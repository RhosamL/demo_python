import random

# Function to generate a hint
def generate_hint(secret_word, user_guess):
    hint = ""
    for i in range(len(secret_word)):
        if secret_word[i] == user_guess[i]:
            hint += secret_word[i].upper()
        elif user_guess[i] in secret_word:
            hint += user_guess[i].lower()
        else:
            hint += "_"
    return hint

# Main game loop
def word_guessing_game(secret_word):
    print("Welcome to the word guessing game!")
    hint = "_" * len(secret_word)
    guesses = 0

    while hint != secret_word:
        print(f"Your hint is: {hint}")
        user_guess = input("What is your guess? ").lower()

        if len(user_guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
            guesses += 1
        else:
            guesses += 1
            hint = generate_hint(secret_word, user_guess)

    print(f"Congratulations! You guessed it!\nIt took you {guesses} guesses.")

# Generate a random secret word (you can change this)
secret_word = "mosiah"

# Start the game
word_guessing_game(secret_word)
