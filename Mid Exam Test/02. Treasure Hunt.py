treasures = input().split("|")
command = input()
stolen = []
length = 0
while not command == "Yohoho!":
    action = command.split()

    if action[0] == "Loot":
        for idx in range(1, len(action)):
            if not action[idx] in treasures:
                treasures.insert(0, action[idx])

    elif action[0] == "Drop":
        idx = action[1]
        idx = int(idx)
        if not idx > len(treasures)-1:
            x = treasures[idx]
            treasures.pop(idx)
            treasures.append(x)

    # elif action[0] == "Steal":
    #     count = action[1]
    #     count = int(count)
    #     for idx in range(-1, -count, -1):
    #         stolen.append(treasures[idx])
    #         treasures.pop(idx)
    #     print(", ".join(str(item)for item in stolen))

    command = input()

if len(treasures) > 0:
    for item in treasures:
        length += len(item)
        length /= len(treasures)
    print(f"Average treasure gain: {length} pirate credits.")
else:
    print("Failed treasure hunt.")
