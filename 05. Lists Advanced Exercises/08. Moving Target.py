targets1 = input().split()
command = input()
targets2 = [int(num) for num in targets1]

while command != "End":
    action, idx, value = command.split()
    idx = int(idx)
    value = int(value)

    if action == "Shoot":
        if 0 <= idx <= len(targets1) - 1:
            targets2[idx] -= value
        #if 0 <= idx <= len(targets1) - 1:
            if targets2[idx] <= 0:
                targets2.pop(idx)
    elif action == "Add":
        if 0 <= idx <= len(targets1) - 1:
            targets2.insert(idx, value)
        else:
            print(f"Invalid placement!")
    elif action == "Strike":
        if value *2 +1 < len(targets1) - 1:
            for index in range(idx-value, idx+value):
                if index < len(targets1) - 1:
                    targets2.pop(idx-value)
        else:
            print("Strike missed!")

    command = input()
targets2 = [str(num) for num in targets2]
print("|".join(targets2))