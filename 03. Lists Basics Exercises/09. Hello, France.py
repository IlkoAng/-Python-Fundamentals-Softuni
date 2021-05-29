items = input().split("|")
budget = float(input())
profit = 0
total = 0
my_list = []
for item in items:
    sep = item.split("->")
    type = sep[0]
    price = float(sep[1])

    if type == "Clothes":
        if price > 50:
            continue
    elif type == "Shoes":
        if price > 35:
            continue
    elif type == "Accessories":
        if price > 20.50:
            continue
    if budget < price:
        continue

    budget -= price
    profit += (price * 0.4)
    profit2 = (price * 0.4)
    price += profit2
    my_list.append(f"{price:.2f}")

    total += price
total += budget

print(" ".join(my_list))

print(f"Profit: {profit:.2f}")
if total >= 150:
    print("Hello, France!")
else:
    print("Time to go.")