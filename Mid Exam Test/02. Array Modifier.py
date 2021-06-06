numbers = [int(num) for num in input().split()]
command = input()
index1 = 0
index2 = 0
while not command == "end":
    if command == "decrease":
        action = command
    else:
        action, index1, index2 = command.split()
    index1 = int(index1)
    index2 = int(index2)

    if action == "swap":
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

    elif action == "multiply":
        numbers[index1] = numbers[index1] * numbers[index2]

    elif action == "decrease":
        numbers = [num - 1 for num in numbers]

    command = input()

numbers = [str(num) for num in numbers]
print(", ".join(numbers))