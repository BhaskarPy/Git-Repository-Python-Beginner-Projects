import random
num = random.randint(1,10)
count = 1
temp = 0
print("Machine has guessed the number. Its your turn to guess.")
while count<=3:
    print("Guess %d :: "%count)
    guess = int(input("Enter the number :: "))
    if guess == num:
        temp+=1
        break
    count+=1
if temp == 0:
    print("Alas ! You have lost the game.")
    print("Machine has choosen the number :: %d"%num)
else:
    print("Hurray ! You have won.")