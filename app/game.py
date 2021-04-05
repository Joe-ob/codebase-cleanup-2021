
from random import choice

#
# USER SELECTION
#
VALID_OPTIONS=["rock", "paper", "scissors"]
u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == c:
    print("It's a Tie")
if u == "rock":
    if c == "paper":
        print("The Computer Wins")
    elif c == "scissors":
        print("The User Wins")
if u == "paper":
    if c == "rock":
        print("The User Wins")
    elif c == "scissors":
        print("The Computer Wins")
if u == "scissors":
    if c == "rock":
        print("The Computer Wins")
    elif c == "paper":
        print("The User Wins")


