names = set()

while True:
    name = input("Give name: ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("Syötetyt nimet:")
for name in names:
    print(name)