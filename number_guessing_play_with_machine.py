import random
import sys,os
from time import sleep
choice = "y"
def userTurn():
    os.system('cls')
    print("User turn ")
    num = random.randint(1,10)
    count = 1
    temp = 0
    while count<=3:
        print("Guess number %d :: "%count)
        guess = int(input("Guess any number :: "))
        if guess == num:
            temp+=1
            break
        count+=1
    if temp == 0:
        print("Alas you have lost the game.")
        print("Machine has guessed %d"%num)
    else:
        print("Hurray you have guessed right.")
        sleep(2)
def machineTurn():
    os.system('cls')
    print("Machine turn ")
    num = int(input("Give a number to machine "))
    count = 1
    temp = 0
    while count<=3:
        print("Guess number %d :: "%count)
        guess = random.randint(1,10)
        print("Machine has gussed %d"%guess)
        if guess == num:
            temp+=1
            break
        count+=1
    if temp == 0:
        print("Alas machine has lost the game.")
        print("User has given %d"%num)
    else:
        print("Hurray machine has guessed right.")
        sleep(2)
while choice == "y":
    userTurn()
    machineTurn()
    choice = input("Do you want to continue ? Enter y or n :: ")
    choice.lower()
    sleep(2)