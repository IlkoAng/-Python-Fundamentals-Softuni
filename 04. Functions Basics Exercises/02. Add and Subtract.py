def sum_number(num1, num2):
     return num1 + num2


def subtract(num1, num2, num3):
    return sum_number(num1, num2) - num3


def add_and_subtract(num1, num2, num3):
    return subtract(num1, num2, num3)


number_one = int(input())
number_two = int(input())
number_three = int(input())
print(add_and_subtract(number_one, number_two, number_three))
