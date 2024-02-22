#Creativity: I used a special function: 'end=' to join my looped underscores in line 10, 25, etc.
#I made the game more interactive with game-like prompts.
#I shortened my code by using len(rpuzzle) instead of creating a variable

secret_word = "nigeria"
secret_length = len(secret_word)
aa = 1
#trying to do initial hint. Use for loop, 
print("welcome to the country--word puzzle. You have been given an initial hint:")
for index in range(secret_length):
    under_score = "_"
    print(f"{under_score}", end= " ")

puzzle = input("\n \nTo start, guess a country (the hint has the spaces for the required letters): ")
rpuzzle = puzzle.lower()

#Use while loop! it'll continue until... Body of main code
while puzzle != secret_word:
    aa = aa + 1

    if len(rpuzzle) != len(secret_word):
        print("\nError: Your guess should have the same length as the secret country.")
    else:
        print("Your hint is: ")
        for index in range(secret_length):
            under_score = "_"
            print(f"{under_score}", end = " ")
        
        for index in range(secret_length):

            if rpuzzle[index] == secret_word[index]:
                print(rpuzzle[index].upper(), end = " ")

            elif rpuzzle[index] in secret_word:
                print(rpuzzle[index], end = " ")
            else:
                print("_", end = " ")

    puzzle = input("\nNot Yet! Work your mind and try again, guess the country: ")
    rpuzzle = puzzle.lower()
print(f"Congratulations, you got the right answer ({secret_word}) after {aa} number of trials")