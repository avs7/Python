import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# initialize player moves
player = input("----------Let's play!----------\nType R for ROCK 🪨, P for PAPER 📝 or S for SCISSORS ✂️\n")
computer = ""
result = ""
rand_num = random.randint(0, 2)

if rand_num == 0:
  computer = "Rock"
elif rand_num == 1:
  computer = "Paper"
else:
  computer = "Scissors"


if player == "P" or player == "p":
  print("You chose PAPER 📝")
  print(paper)
  if computer == "Scissors":
    result = "You lost! 😭 "
  elif computer == "Rock":
    result = "You won! 🤗 "
  else:
    result = "It's a Draw  😐 "

elif player == "R" or player == "r":
  print("You chose ROCK 🪨")
  print(rock)
  if computer == "Paper":
    result = "You lost! 😭 "
  elif computer == "Scissors":
    result = "You won! 🤗 "
  else:
    result = "It's a Draw  😐 "

elif player == "S" or player == "s":
  print("You chose SCISSORS ✂️")
  print(scissors)
  if computer == "Rock":
    result = "You lost! 😭 "
  elif computer == "Paper":
    result = "You won! 🤗 "
  else:
    result = "It's a Draw  😐 "
else:
  print("Invalid entry")
  player = input("Let's play!\nType R for ROCK, P for PAPER or S for SCISSORS")

print(f"Computer chose {computer}\n")
print(result)