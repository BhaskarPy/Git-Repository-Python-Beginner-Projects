import random
import sys,os
from time import sleep
import getpass
choice = "y"
def playerOne():
    os.system('cls')
    print("Player one turn ")
    num = int(getpass.getpass(prompt="Give the number to guess :: "))
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
        print("Alas player one has lost the game.")
        print("Player two has given %d"%num)
    else:
        print("Hurray player one guessed right.")
        sleep(2)
def playerTwo():
    os.system('cls')
    print("Player two turn ")
    num = int(getpass.getpass(prompt="Give the number to guess :: "))
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
        print("Alas player two has lost the game.")
        print("Player one has given %d"%num)
    else:
        print("Hurray player has guessed right.")
        sleep(2)
while choice == "y":
 playerOne()
 playerTwo()
 choice = input("Do you want to continue ? Enter y or n :: ")
 choice.lower()
 sleep(2)