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
  move = input("Type 'y' to get another card, type 'n' to pass: ")
  return move

def play():
  #for testing
  print(computer)
  totals()
  print(f"     Your cards: {player}, current score: {player_total}\n     Computer's first card: {computer[0]}")
  decision()
  if move == 'n':
    display_result()
  elif move == 'y':
    draw_card()
    if player_total < 21:
      play()
    else:
      pick_winner()
      display_result()

def pick_winner():
  winner = ""
  if player_total > computer_total and player_total <= 21:
    winner = 'player'
  elif player_total < computer_total or player_total > 21:
    if player_total < computer_total:
      winner = 'player'
    elif player_total > computer_total:
      winner = 'computer'
  else:
    winner = "tie"
  return winner

def display_result():
  if pick_winner() == 'player':
    print(f"\nComputer had: {computer}")
    print(f"You had: {player}\n")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
    print("◦   YOU WIN!  ◦")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
  elif pick_winner() == 'computer':
    print(f"\nComputer had: {computer}\n")
    print(f"You had: {player}")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
    print("◦  YOU LOST!  ◦")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
  elif pick_winner() == 'tie':
    print(f"\nComputer had: {computer}\n")
    print(f"You had: {player}")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
    print("◦ IT'S A TIE! ◦")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")

  again = input("Would you like to play again? 'y' or 'n': ")
  if again == 'y':
    deal()
    play()
  elif again == 'n':
    os.system('cls')

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
    #display_result()
  elif player_total < 21:
    play()

print(logo)
deal()
play()