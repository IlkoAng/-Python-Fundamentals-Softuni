command = input()
mydict = {}

while not command == "End":
    name, number = command.split(" -> ")

    if name not in mydict:
        mydict[name] = [number]
    else:
        if number not in mydict[name]:
            mydict[name] += [number]

    command = input()

sorted_companies = dict(sorted(mydict.items(), key=lambda kvp: (kvp[0])))

for key, value in sorted_companies.items():
    print(f"{key}")
    for number in value:
        print(f"-- {number}")
