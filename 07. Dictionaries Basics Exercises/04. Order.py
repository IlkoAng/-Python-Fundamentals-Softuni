command = input()
products = {}

while not command == "buy":
    item, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if item not in products:
        products[item] = {"price": price, "quantity": quantity}
    else:
        products[item]["price"] = price
        products[item]["quantity"] += quantity

    command = input()

for key, value in products.items():
    result = value["price"] * value["quantity"]
    print(f"{key} -> {result:.2f}")