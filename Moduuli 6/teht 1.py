import random
def roll_dice():
    while True:
        dice = random.randint(1, 6)
        print(dice)
        if dice == 6:
            break
roll_dice()