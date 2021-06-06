targets = [int(num) for num in input().split()]

command = input()

while not command == "End":
    action, index, value = command.split()
    index = int(index)
    value = int(value)

    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")

    elif action == "Strike":
        if index + value < len(targets) and index - value >= 0:
            #targets = targets[:index - value] + targets[index + value + 1:]
            x = targets[index]
            for num in range(index - value, index + value):
                targets.pop(num)
            targets.remove(x)
        else:
            print("Strike missed!")

    command = input()

targets = [str(num) for num in targets]
print("|".join(targets))
