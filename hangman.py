import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

words_file = open("words.txt", "r")
data = words_file.read()
words_list = data.split("\n")

lives = 7
guess_arr = []
wrong_guesses =[]
wrong_word = ""
word = random.choice(words_list)
game_over = False

print(logo)
print(word)

for _ in word:
  guess_arr.append("_")
guess_word = "  ".join(guess_arr)
print(f"\n   WORD: {guess_word}   \n\n")

while not game_over:
  guess = input("Guess a letter: ").lower()
  if guess in word:
    print("Good guess!")
    for position in range(len(word)):
      if word[position] == guess:
        guess_arr[position] = guess
        guess_word = "  ".join(guess_arr)
        print(f"\n   WORD: {guess_word}   \n\n")
  else:
    lives -= 1
    if lives > 0:
      wrong_guesses += guess
      wrong_word = "  ".join(wrong_guesses)
      print(stages[lives])
      print(f"\nWrong letters: {wrong_word}")
      print(f"\n   WORD: {guess_word}   \n\n")
      print(f"Bad guess! You have {lives} lives left\n")
    else:
      print("\n ❗❗❗ You lose! ❗❗❗ ")
      print(stages[lives])
      game_over = True
  
  if "_" not in guess_arr:
    game_over = True
    print("You win!")