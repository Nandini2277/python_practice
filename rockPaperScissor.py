import random

def get_choices():
    player_choice = input("Enter a choice; rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes Scissors, you win!!"
        else:
            return "Paper covers Rock, you lose. ;_;"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cut Paper, you lose. ;_;"
        else:
            return "Paper covers Rock, you win!!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes Scissors, you lose ;_;"
        else: 
            return "Scissors cut Paper, you win!!"

choices=get_choices()
result=check_win(choices["player"], choices["computer"])
print(result)