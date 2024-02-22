#Completing the activity:

#word = "commitment"
#favor = input("what's your favourite alphabet?: ")
#for letter in word:
#    if letter.lower() == favor.lower():
#        print(letter.upper(), end="")
#    else:
#        print(letter.lower(), end="")
#print()
#for letter in word:
#    if letter.lower() == favor.lower():
#        print("_", end="")
#    else:
#        print(letter, end="")


#Redoing the activity:
words = "commitment"
favourite_alphabet = input("What's your favorite alphabet? ")
word_length = len(words)

for index in range(word_length):
    wording = words[index]
    if wording.lower() == favourite_alphabet.lower():
        mwording = "_"
        print(f"Numbers: {index} letters: {mwording}")
    else:
        print(f"Numbers: {index} letters: {wording}")