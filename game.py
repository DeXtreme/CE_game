import random

print("### Welcome to the Rock, Paper, Scissors game ###")
print("Here are the rules: Every turn you decide what to play")
print("Rock beats Paper, Paper beat Rock, Rock beats Scissors")

choices = ['Rock','Paper','Scissors']
player_choice = ""

your_score = 0
computer_score = 0

print("### Let the games begin ###")

while True:
    player_choice = input("Make a choice : ")

    if player_choice not in choices:
        print("Hey that's not allowed!")
        continue

    computer_choice = random.choice(choices)
    print("Computer plays", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie")
    elif player_choice == 'Rock' and computer_choice == 'Scissors':
        print("You win!")
        your_score = your_score + 1
    elif player_choice == 'Paper' and computer_choice == 'Rock':
        print('You win')
        your_score = your_score + 1
    elif player_choice == 'Scissors' and computer_choice == 'Paper':
        print('You win')
        your_score = your_score + 1
    else:
        print('You lost')
        computer_score = computer_score + 1
    
    print("You :",your_score,"   ", computer_score,": Computer")
    
    new_game = input('Play again?(Y/N) :')
    
    if new_game == 'N':
        break
    





