import random

choices = ["rock", "paper", "scissors"]

user = input("Enter rock/paper/scissors: ")
computer = random.choice(choices)

print("Computer:", computer)

if user == computer:
    print("Tie")

elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win")

else:
    print("Computer wins")