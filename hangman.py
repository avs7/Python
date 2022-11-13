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
easy = []
medium = []
hard = []
wrong_word = ""
game_over = False

for word in words_list:
  if len(word) <= 3 and len(word) > 2:
    easy.append(word)
  elif len(word) > 3 and len(word) <= 5:
    medium.append(word)
  else:
    hard.append(word)


print(logo)
difficulty = input("\n***** Select level: 1 - Easy, 2 - Medium, 3 - Hard *****\n")

if difficulty == "1":
  word = random.choice(easy)
elif difficulty == "2":
  word = random.choice(medium)
elif difficulty == "3":
  word = random.choice(hard)
else:
  print("Invalid entry!")
  difficulty = input(int("\n***** Select level: 1 - Easy, 2 - Medium, 3 - Hard *****\n"))

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