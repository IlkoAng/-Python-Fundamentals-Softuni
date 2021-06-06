dungeon_rooms = input().split("|")
health = 100
bitcoin = 0
counter = 0
isEnough = True
for rooms in dungeon_rooms:
    command, number = rooms.split()
    number = int(number)
    counter += 1

    if command == "potion":
        if health + number > 100:
            x = abs(health - 100)
            health += number
            y = health - 100
            health -= y
            print(f"You healed for {x} hp.")
            print(f"Current health: {health} hp.")
        else:
            health += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if not health <= 0:
            print(f"You slayed {command}.")
        elif health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {counter}")
            isEnough = False
            break

if isEnough:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")