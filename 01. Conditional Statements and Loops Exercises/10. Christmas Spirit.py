quantity = int(input())
days = int(input())
spirit = 0
cost = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for day in range(1, days +1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        cost += (ornament_set * quantity)
        spirit += 5
    if day % 3 == 0:
        cost += (tree_skirt * quantity)
        cost += (tree_garlands * quantity)
        spirit += 13
    if day % 5 == 0:
        cost += (tree_lights * quantity)
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        cost += (tree_skirt + tree_lights + tree_garlands)
        if day == days:
            spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
