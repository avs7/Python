import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

auction = True
bids = {}
highest_bidder = ""
highest_bid = 0


while auction:
  name = input("\nEnter your name: ")
  bid = int(input("Enter bid: $"))
  bids[name] = bid
  more_bids = input("Are there other bidders? (y or n): ")

  if more_bids.lower() == "n":
    auction = False
    os.system('cls')
  elif more_bids.lower() == "y":
    os.system('cls')

for bidder in bids:
  if bids[bidder] >= highest_bid:
    highest_bid = bids[bidder]
    highest_bidder = bidder

print(f"\nThe winner is {highest_bidder} with a bid of {highest_bid}")