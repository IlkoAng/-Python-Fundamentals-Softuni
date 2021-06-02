elements = input().split(" ")
bakery = {}

for x in range(0, len(elements), 2):
    key = elements[x]
    value = elements[x + 1]
    bakery[key] = int(value)

searched = input().split()

for key in searched:
    if key in bakery:
        print(f"We have {bakery[key]} of {key} left")
    else:
        print(f"Sorry, we don't have {key}")