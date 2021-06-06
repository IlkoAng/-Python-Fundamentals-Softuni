price = input()
total = 0
price_without_taxes = 0
taxes = 0
isTrue = True
while price != "special" and price != "regular":

    if float(price) < 0:
        price = input()
        print("Invalid price!")
        continue

    else:
        price_without_taxes += float(price)
        taxes += float(price) * 0.2

    price = input()

total = price_without_taxes + taxes

if price == "special":
    discount = total * 0.1
    total -= discount

if total == 0:
    print("Invalid order!")
    isTrue = False

if isTrue:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total:.2f}$")

