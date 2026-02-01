numbers = []
while True:
    syote = input("Enter a number: ")
    if syote == "":
        break
    numbers.append(float(syote))
numbers.sort(reverse=True)
print("The greatest numbers in descending order: ")
for number in numbers[:5]:
    print(number)