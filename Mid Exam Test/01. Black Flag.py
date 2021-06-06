days = int(input())
plunder_per_day = int(input())
needed_plunder = float(input())
total = 0


for day in range(1, days+1):
    total += plunder_per_day

    if day % 3 == 0:
        bonus = plunder_per_day * 0.5
        total += bonus

    if day % 5 == 0:
        lost = total * 0.3
        total -= lost

percentage = (total / needed_plunder) * 100

if total >= needed_plunder:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")


