fire = input().split("#")
water = int(input())
effort = 0
total_fire = 0
my_list = []
for cell in fire:
    sep = cell.split(" = ")
    type = sep[0]
    level = int(sep[1])
    if type == "High":
        if not 81 <= level <= 125:
            continue
    elif type == "Medium":
        if not 51 <= level <= 80:
            continue
    elif type == "Low":
        if not 1 <= level <= 50:
            continue
    if water < level:
        continue

    my_list.append(level)
    water -= level
    effort += (level * 0.25)
    total_fire += level

print("Cells:")
for levels in my_list:
    print(f" - {levels}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")