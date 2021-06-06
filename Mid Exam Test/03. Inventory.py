items = input().split(", ")
command = input()

while command != "Craft!":
    action, item = command.split(" - ")

    if action == "Collect":
        if item not in items:
            items.append(item)

    elif action == "Drop":
        if item in items:
            items.remove(item)

    elif action == "Combine Items":
        old, new = item.split(":")
        if old in items:
            x = items.index(old)
            items.insert(x+1, new)
        else:
            continue

    elif action == "Renew":
        if item in items:
            x = items.index(item)
            y = items.pop(x)
            items.append(item)
    command = input()
print(", ".join(items))