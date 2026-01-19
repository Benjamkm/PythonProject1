gend = input("Enter biological gender (male/female): ").lower()
if gend != "male" and gend != "female":
    print("Invalid gender.")
else:
    hemo = float(input("Enter hemoglobin value (g/l): "))
if gend == "female":
    if hemo < 117:
        print("Your hemoglobin is low.")
    elif 117 <= hemo <= 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")
if gend == "male":
    if hemo < 134:
        print("Your hemoglobin is low.")
    elif 134 <= hemo <= 167:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")