kuha = float(input("Enter the length of the zander in centimeters: "))
if kuha < 42:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {42 - kuha:.1f} centimeters below the size limit.")
if kuha >= 42:
  print("The zander meets the size limit.")