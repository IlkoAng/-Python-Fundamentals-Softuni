elements = input().split(" ")
bakery = {}

for x in range(0, len(elements), 2):
    key = elements[x]
    value = elements[x + 1]
    bakery[key] = int(value)
print(bakery)