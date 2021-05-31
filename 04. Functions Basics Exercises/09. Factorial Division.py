def factorial(n1, n2):

    for num_first in range(n1-1, 0, -1):
        n1 *= num_first

    for num_second in range(n2-1, 0, -1):
        n2 *= num_second

    result = n1 / n2
    return result


num1 = int(input())
num2 = int(input())
result = factorial(num1, num2)
print(f"{result:.2f}")
