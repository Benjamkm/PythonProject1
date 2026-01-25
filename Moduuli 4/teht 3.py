pienin = None
suurin = None

while True:
    num = input("Enter a number (or press Enter to quit): ")
    if num == "":
        break
    luku = float(num)
    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku
print("Smallest number:", pienin)
print("Largest number:", suurin)