while True:
    tuuma = float(input("Enter length in inches (negative value to quit): "))
    if tuuma < 0:
        print("Program ended.")
        break
    cm = tuuma * 2.54
    print(f"{tuuma:.1f} inches is {cm:.2f} centimeters")