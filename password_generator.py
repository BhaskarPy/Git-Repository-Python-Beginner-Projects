import random
import os
upper = []
lower = []
pswrd = []
blank = ['u','l','n','sp']
num = [0,1,2,3,4,5,6,7,8,9]
sp = ['#','@','%','&','^','!','~']
for i in range(65,91):
    upper.append(chr(i))
for i in range(97,123):
    lower.append(chr(i))
os.system('cls')
count = int(input("How many characters long password , do you want ? :: "))
i=0
while i<=count:
    index=random.randint(0,3)
    ch=blank[index]
    if ch=='u':
        index=random.randint(0,25)
        ch=upper[index]
        pswrd.append(ch)
        i+=1
    elif ch=='l':
        index=random.randint(0,25)
        ch=lower[index]
        pswrd.append(ch)
        i+=1
    elif ch=='n':
        index=random.randint(0,9)
        ch=num[index]
        pswrd.append(ch)
        i+=1
    elif ch=='sp':
        index=random.randint(0,6)
        ch=sp[index]
        pswrd.append(ch)
        i+=1

print("Your password ::",end=" ")
for i in pswrd:
    print(i,end='')

