import random
luku = random.randint(1, 10)
while True:
    syote = int(input("Guess a number (1-10):" ))
    if luku == syote:
        print("Correct")
        break
    elif syote < luku:
        print("Too low")
    elif syote > luku:
        print("Too high")