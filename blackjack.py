import random
import numpy
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#infinite deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer = []
player = []
player_total = 0
computer_total = 0
move = ''
winner = ''

def totals():
  global player_total
  global computer_total
  player_total = numpy.sum(player)
  computer_total = numpy.sum(computer)

def deal():
  global player
  global computer
  player = []
  computer = []

  while len(computer) < 2:
    player.append(random.choice(cards))
    computer.append(random.choice(cards))
  if computer[0] + computer[1] <= 17:
    computer.append(random.choice(cards))

def decision():
  global move
  print(f"     Your cards: {player}, current score: {player_total}\n     Computer's first card: {computer[0]}\n")
  move = input("Type 'y' to get another card, type 'n' to pass: ")
  return move

def play():
  #for testing
  print(f"\n{computer}\n")

  totals()
  decision()
  if move == 'n':
    pick_winner()
    display_result()
  elif move == 'y':
    draw_card()

def again():
  play_again = input("Would you like to play again? 'y' or 'n': ")
  if play_again == 'y':
    deal()
    play()
  elif play_again == 'n':
    os.system('cls')

def pick_winner():
  global winner
  if player_total > computer_total and player_total <= 21:
    winner = 'player'
  elif player_total < computer_total or player_total > 21:
    if player_total < computer_total:
      winner = 'player'
    elif player_total > computer_total:
      winner = 'computer'
  else:
    winner = "tie"

def display_result():
  if winner == 'player':
    print(f"\nComputer had: {computer}")
    print(f"You had: {player}\n")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
    print("◦   YOU WIN!  ◦")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
  elif winner == 'computer':
    print(f"\nComputer had: {computer}\n")
    print(f"You had: {player}")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
    print("◦  YOU LOST!  ◦")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
  elif winner == 'tie':
    print(f"\nComputer had: {computer}\n")
    print(f"You had: {player}")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
    print("◦ IT'S A TIE! ◦")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
  again()

def draw_card():
  global player
  new_card = random.choice(cards)
  if new_card == 11:
    choice = input("You got an ACE. Type '1' or '11': ")
    if choice == "1":
      player.append(1)
    elif choice == "11":
      player.append(11)
  else:
    player.append(new_card)
  totals()
  if player_total >= 21:
    pick_winner()
    display_result()
  elif player_total < 21:
    play()

print(logo)
deal()
play()