import random
design=["-------","|     |","|     O","|    /|\\","|    / \\","|      ","-------"]
index=random.randint(0,11)
wl=["ability",
    "advance",
    "billion",
    "brother",
    "captain",
    "company",
    "desktop",
    "digital",
    "excited",
    "fortune",
    "gallery",
    "improve"]
word=wl[index]
lst=list(word)
print(word)
count=0
wrong=0
gw=["_","_","_","_","_","_","_"]
for count in range(0,7):
    print("Round :: ",count+1)
    guess=input("Guess the letter :: ").strip()
    if guess==lst[count]:
        print("Hurray ! You have guessed right.")
    else:
        print("Alas ! You have guessed wrong.")
        for i in range(0,wrong+1):
            print(design[i])
        wrong+=1