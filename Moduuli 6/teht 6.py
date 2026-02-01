import math

def calculate_unit_price(diameter, price):
    radius_m = (diameter / 100) / 2
    area = math.pi * radius_m ** 2
    return price / area

first_diameter = float(input("Enter the diameter of the first pizza (cm): "))
first_price = float(input("Enter the price of the first pizza (euros): "))
second_diameter = float(input("Enter the diameter of the second pizza (cm): "))
second_price = float(input("Enter the price of the second pizza (euros): "))

first_price_m = calculate_unit_price(first_diameter, first_price)
second_price_m = calculate_unit_price(second_diameter, second_price)
print(f"Unit price of the first pizza: {first_price_m:.2f} euros/m²")
print(f"Unit price of the second pizza: {second_price_m:.2f} euros/m²")
if first_price_m < second_price_m:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")