def get_season(month):
    if month in (12, 1, 2):
        return "winter"
    elif month in (6, 7, 8):
        return "summer"
    elif month in (9, 10, 11):
        return "autumn"
    elif month in (3, 4, 5):
        return "spring"
    else:
        return None

month = int(input("Enter the number of a month (1-12): "))
season = get_season(month)
if season is None:
    print(f"You entered: {month} \nPlease enter a number between 1 and 12.")
else:
    print(f"You entered: {month} \nThe season is {season}.")