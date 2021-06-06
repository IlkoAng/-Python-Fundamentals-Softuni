neighborhood = [int(num) for num in input().split("@")]
length = 0
command = input()

while not command == "Love!":
    love, index = command.split()
    index = int(index)
    length += index

    if len(neighborhood) > length:
        if neighborhood[length] <= 0:
            print(f"Place {length} already had Valentine's day.")
        else:
            neighborhood[length] -= 2
            if neighborhood[length] <= 0:
                print(f"Place {length} has Valentine's day.")

    else:
        length = 0
        if neighborhood[length] <= 0:
            print(f"Place {length} already had Valentine's day.")
        else:
            neighborhood[length] -= 2
            if neighborhood[length] <= 0:
                print(f"Place {length} has Valentine's day.")

    command = input()

counter = 0
for num in neighborhood:
    if num > 0:
        counter += 1

print(f"Cupid's last position was {length}.")
if counter == 0:
    print("Mission was successful.")
elif counter > 0:
    print(f"Cupid has failed {counter} places.")
