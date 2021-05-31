def orders(product, piece):
    result = None
    if product == "coffee":
        return 1.50 * piece
    elif product == "water":
        return piece
    elif product == "coke":
        return 1.40 * piece
    elif product == "snacks":
        return 2.00 * piece



items = input()
quantity = int(input())
result = orders(items, quantity)
print(f"{result:.2f}")