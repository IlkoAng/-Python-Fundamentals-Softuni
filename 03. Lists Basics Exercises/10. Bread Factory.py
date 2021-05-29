events = input().split("|")
energy = 100
coins = 100
#my_list = []
isEnough = False
for event in events:
    sep = event.split("-")
    item = sep[0]
    number = int(sep[1])
    #my_list.append(event)
    if item == "rest":
        energy += number
        if energy > 100:
            energy -= number
            print("You gained 0 energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")

    elif item == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {item}.")
        elif coins < number:
            isEnough = True
            break


if isEnough:
    print(f"Closed! Cannot afford {item}.")

else:
    #len(events) == len(my_list) and energy > 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


