def sum_of_list(number_list):
    summa = 0
    for number in number_list:
        summa += number
    return summa
number_list = [1, 2, 3, 4, 5]
result = sum_of_list(number_list)
print(f"The sum of the numbers in the list is: {result}")