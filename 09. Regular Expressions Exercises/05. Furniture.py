import re
order = input()
regex = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
total = 0
names = []
while not order == "Purchase":

    valids = re.match(regex, order)
    if valids:
        data = valids.groupdict()
        names.append(data["name"])
        total += float(data["price"]) * int(data["quantity"])
    order = input()

print("Bought furniture:")
if names:
    print("\n".join(names))
print(f"Total money spend: {total:.2f}")

