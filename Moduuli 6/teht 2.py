import random
tahko = int(input("Anna nopan tahkojen määrä"))
def roll_dice(tahko):
    while True:
        dice = random.randint(1, tahko)
        print(dice)
        if dice == tahko:
            break
roll_dice(tahko)