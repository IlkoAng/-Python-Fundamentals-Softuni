def smallest(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    elif num3 < num1 and num3 < num2:
        return num3


number_one = int(input())
number_two = int(input())
number_three = int(input())
print(smallest(number_one, number_two, number_three))