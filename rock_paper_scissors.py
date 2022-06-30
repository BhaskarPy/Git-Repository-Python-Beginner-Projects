import os
while True:
    os.system('cls')
    print("Player 1 turn..")
    guess1=input("Enter 'r' for rock, 'p' for paper, 's' for scissors :: ").strip()
    print("Player 2 turn..")
    guess2=input("Enter 'r' for rock, 'p' for paper, 's' for scissors :: ").strip()
    if guess1=='r' and guess2=='s':
        print("player 1 wins")
    elif guess1=='p' and guess2=='r':
        print("player 1 wins")
    elif guess1=='s' and guess2=='p':
        print("player 1 wins")
    elif guess2=='r' and guess1=='s':
        print("player 2 wins")
    elif guess2=='p' and guess1=='r':
        print("player 2 wins")
    elif guess2=='s' and guess1=='p':
        print("player 2 wins")
    choice=input("Do you want you continue ? Type y/n :: ").strip()
    if choice=='n':
        break

    