import random

temp_words = ["hot", "cold", "dog", "cat", "house", "mouse", "random"]

def new_game():
  rand_index = random.randint(0, len(temp_words) - 1)
  word = temp_words[rand_index]
  word_arr = list(word)
  guess_arr = []
  for letter in word_arr:
    guess_arr.append("_")
  guess_word = "  ".join(guess_arr)

  print("********** Let's play hangman **********")
  print(word)
  print(f"\n   WORD: {guess_word}   \n\n")
  guess = input("Guess a letter: ")

  if guess.lower() in word_arr:
    print("good guess")
  else:
    print("bad guess")

  print(guess)
  

new_game()