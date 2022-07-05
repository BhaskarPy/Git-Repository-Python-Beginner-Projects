"""
Logic of the game -
Player 1 will give - X and player 2 will give O.
ASCII value of X is 88 and O is 79.
So, we will check which key-value pair of a dictionary has 88 or 79 in it.
If player 1 wins , that means sum of the three cells would be 264(88+88+88).
If player 2 wins , that means sum of the three cells would be 237(79+79+79).
We will check for these sums.
If these sums are not generated, then game is a draw.
"""
import sys
# Creating blank dictionary which key will hold position and value will hold user input
game={}
# Creating list of tuples
# If these triplets have X or O, player will win
# E.g. if 1,2,3 position has X in them, then player 1 will win
p=[
    (1,2,3),
    (4,5,6),
    (7,8,9),
    (1,4,7),
    (2,5,8),
    (3,6,9),
    (1,5,9),
    (3,5,7) 
]
# A blank list which will help to check whether the game is drawn or not
res=[]
# Adding keys and values to the dictionary
k=1
for i in range(1,10):
    game[i]=k
    k+=1
# Function to check whether the game is drawn or not.
def gameDraw() :
    for i in p:
        s=0
        for j in i:
            s+=game[j]
            res.append(s)
    x,y=264,237
    if (x not in res) or (y not in res):
        printGame()
        print("Game Draw.")
        sys.exit()
# Function to print grid like structure of the game.
def printGame():
    k=1
    for i in range(1,4):
        for j in range(1,4):
            if game[k]==79 or game[k]==88:
                print(chr(game[k])," | ",end="")
                k+=1
            else:
                print(game[k]," | ",end="")
                k+=1
        print("\n")
    return
# Function for player 1
def playerOne():
    printGame()
    print("Now player 1 turn")
    p1=int(input("Select a cell :: "))
    # ASCII of "X" is 88 and "O" is 79
    if game[p1]==88 or game[p1]==79:
        print("Cell already occupied. Select another cell.")
        p1=0
        playerOne()
    if p1 in game:
        game[p1]=88
    checkResult(game)
    return
# Function for player 2.
def playerTwo():
    printGame()
    print("Now player 2 turn")
    p2=int(input("Select a cell :: "))
    # ASCII of "X" is 88 and "O" is 79
    if game[p2]==88 or game[p2]==79:
        print("Cell already occupied. Select another cell.")
        p2=0
        playerTwo()
    if p2 in game:
        game[p2]=79
    checkResult(game)
    return
# Function to check the result
def checkResult(game):
    for i in p:
        s=0
        for j in i:
            s=s+game[j]
        # 264=X+X+X, 237=O+O+O sum of ASCII
        if s==264:
            printGame()
            print("Player 1 wins")
            sys.exit()
        elif s==237:
            printGame()
            print("Player 2 wins")
            sys.exit()
    s=0
    for i in game:
        if game[i]==79 or game[i]==88:
            s+=1
    if s==9:
        gameDraw()
    else:
        return
# Main function
while True:
    playerOne()
    playerTwo()
    
    
