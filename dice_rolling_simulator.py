# Import Modules
import time
import os
import random
import sys

# Create function
def playGame():
    time.sleep(1)
    n=random.randint(1,6)
    if n==1:
        print("You have got :: \n")
        print("-------")
        print("       ")
        print("   *   ")
        print("       ")
        print("-------")
    elif n==2:
        print("You have got :: \n")
        print("-------")
        print("*      ")
        print("       ")
        print("      *")
        print("-------")
    elif n==3:
        print("You have got :: \n")
        print("-------")
        print("*      ")
        print("   *   ")
        print("      *")
        print("-------")
    elif n==4:
        print("You have got :: \n")
        print("-------")
        print("*     *")
        print("       ")
        print("*     *")
        print("-------")
    elif n==5:
        print("You have got :: \n")
        print("-------")
        print("*     *")
        print("   *   ")
        print("*     *")
        print("-------")
    elif n==6:
        print("You have got :: \n")
        print("-------")
        print("*     *")
        print("*     *")
        print("*     *")
        print("-------")
    return
        
# Welcome Message
print("###################################")
print()
print(" Welcome to Dice Rolling Simulator ")
print()
print("###################################")
print()
choice=input("Do you want to play the game ? (y/n) :: ").lower()
if choice=='y':
    while True:
        os.system('cls')
        print("Starting to roll the dice")
        playGame()
        opt=input("Do you want to continue ? (y/n) :: ").lower()
        if opt=='y':
            continue
        else:
            sys.exit("See you again.")
else:
    sys.exit("See you again.")


    