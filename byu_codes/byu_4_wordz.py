secret_word = "nigeria"
secret_length = len(secret_word)
puzzle = input("Welcome to puzzle, write a country: ")
rpuzzle = puzzle.lower()

# Check if the length of the guess is the same as the length of the secret word
if len(rpuzzle) != len(secret_word):
        print("\nError: Your guess should have the same length as the secret word.")
else:
    print("Your hint is: _______")
    for index in range(secret_length):

        if rpuzzle[index] == secret_word[index]:
            print(rpuzzle[index].upper(), end=' ')

        elif rpuzzle[index] in secret_word:
            print(rpuzzle[index], end=' ')  # Print in lowercase if it's a correct guess but in the wrong position
        else:
            print("_", end= " ")
# Check if the character in the guess matches the character in the secret_word at the same position
