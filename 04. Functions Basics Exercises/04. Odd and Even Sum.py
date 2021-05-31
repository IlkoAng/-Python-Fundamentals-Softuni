def sum_of_numbers(num):
    even_number = 0
    odd_number = 0
    for dig in num:
        if int(dig) % 2 == 0: #and int(dig) != 0:
            even_number += int(dig)
        else:
            odd_number += int(dig)
    print(f"Odd sum = {odd_number}, Even sum = {even_number}")


number = input()
sum_of_numbers(number)
