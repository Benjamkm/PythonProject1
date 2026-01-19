hytti = input("Enter the cabin class (LUX, A, B, or C): ")
if hytti == "LUX":
  print("Upper-deck cabin with a balcony.")
elif hytti == "A":
    print("Above the car deck, equipped with a window.")
elif hytti == "B":
      print("Windowless cabin above the car deck.")
elif hytti == "C":
        print("Windowless cabin below the car deck.")
else:
         print("Invalid cabin class.")