number = int(input())
capacity = 255
current_tank = 0
for n in range(1, number + 1):
    liters_of_water = int(input())
    current_tank += liters_of_water
    if current_tank > capacity:
        current_tank -= liters_of_water
        print("Insufficient capacity!")
        continue
print(current_tank)