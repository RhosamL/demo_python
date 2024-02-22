#First, trying to make secret word appear as underlines

secret_word = "nigeria"
secret_length = len(secret_word)
puzzle = input("Welcome to puzzle, write a country: ")
rpuzzle = puzzle.lower()

#Now, to check if the length of the guess is the same as length of secret word...
if len(rpuzzle) != len(secret_word):
        print("\nerror message at length of input word")
elif len(rpuzzle) == len(secret_word):
      print("Your hint is...")
      for index in range(len(secret_word)):     
           rsecret = secret_word[index]
           hide_hint = "_"
           print(f"{hide_hint}")   
      for i in range(len(rpuzzle)):
            mpuzzle = rpuzzle[i]

            print(f"secret word {rsecret}, puzzle {mpuzzle}")
#Now, trying to put the puzzle words that match:
            
   

#    aa = range(rpuzzle)
#    aapuzzle = rpuzzle[aa]