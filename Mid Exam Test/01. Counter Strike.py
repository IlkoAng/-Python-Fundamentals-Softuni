energy = int(input())
distance = input()
counter = 0
isEnough = True
while not distance == "End of battle":
    energy -= int(distance)

    if energy < 0:
        energy += int(distance)
        print(f"Not enough energy! Game ends with {counter} won battles and {energy} energy")
        isEnough = False
        break

    counter += 1

    if counter % 3 == 0:
        energy += counter

    distance = input()

if isEnough:
    print(f"Won battles: {counter}. Energy left: {energy}")