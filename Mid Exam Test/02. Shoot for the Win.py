targets = [int(num) for num in input().split(" ")]
idx = input()

while not idx == "End":
    idx = int(idx)

    if idx > len(targets) - 1:
        idx = input()
        continue
    if not targets[idx] == -1:
        for dig in range(len(targets)):
            #z = targets.index(target)
            if not targets[dig] == -1 and not dig == idx:
                if targets[idx] < targets[dig]:
                    #x = targets.index(target)
                    y = targets[dig] - targets[idx]
                    targets.insert(dig, y)
                    targets.pop(dig+1)

                elif targets[idx] >= targets[dig]:
                    #x = targets.index(target)
                    y = targets[dig] + targets[idx]
                    targets.insert(dig, y)
                    targets.pop(dig+1)
        targets[idx] = -1

    idx = input()

targets = [str(num) for num in targets]
counter = 0
for num in targets:
    if num == "-1":
        counter += 1

print(f"Shot targets: {counter} -> {' '.join(targets)}")

