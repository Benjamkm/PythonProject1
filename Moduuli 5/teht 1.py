import random
dice = int(input("How many dice to roll: "))
summa = 0
for i in range(dice):
    heitto = random.randint(1, 6)
    summa += heitto
print("Sum of the dice: ", summa)