def solve(a, b, op):
    result = None
    if op == "multiply":
        result = a * b
    elif op == "divide":
        result = a // b
    elif op == "add":
        result = a + b
    elif op == "subtract":
        result = a - b
    return result


input_operator = input()
first_number = int(input())
second_number = int(input())
print(solve(first_number, second_number, input_operator))
