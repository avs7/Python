import random
import numpy

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

def start():
  while len(computer) < 2:
    player.append(random.choice(cards))
    computer.append(random.choice(cards))
  if computer[0] + computer[1] <= 17:
    computer.append(random.choice(cards))

start()

player_total = numpy.sum(player)
computer_total = numpy.sum(computer)

#for testing
print(computer)

print(f"     Your cards: {player}, current score: {player_total}\n     Computer's first card: {computer[0]}")

move = input("Type 'y' to get another card, type 'n' to pass: ")

def pick_winner():
  winner = ""
  if player_total > computer_total and player_total <= 21:
    winner = 'player'
  elif player_total < computer_total or player_total > 21:
    winner = 'computer'
  else:
    winner = "tie"
  return winner

def display_result():
  if pick_winner() == 'player':
    print(f"\nComputer had: {computer}")
    print(f"You had: {player}")
    print("YOU WIN!")
  elif pick_winner() == 'computer':
    print(f"\nComputer had: {computer}")
    print(f"You had: {player}")
    print("YOU LOST!")
  elif pick_winner() == 'tie':
    print(f"\nComputer had: {computer}")
    print(f"You had: {player}")
    print("IT'S A TIE!")

# def draw_card():

if move == 'n':
  display_result()
elif move == 'y':
  print("test")