def gallons_to_liters(gallona):
    return gallona * 3.785
while True:
    gallon = float(input("Enter a volume in American gallons (negative value to quit): "))
    if gallon < 0:
        print("Program finished. ")
        break
    liters = gallons_to_liters(gallon)
    print(f"{gallon} American gallons is{liters: .2f} liters.")