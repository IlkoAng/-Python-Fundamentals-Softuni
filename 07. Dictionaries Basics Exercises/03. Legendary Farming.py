data = input()
significunt = {"shards": 0, "fragments": 0, "motes": 0}
key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk = {}
isObtained = False

while not isObtained:
    items = data.split()

    for idx in range(0, len(items), 2):

        if isObtained:
            break

        quantity = int(items[idx])
        materials = items[idx+1].lower()

        if materials in significunt:
            significunt[materials] += quantity
        else:
            if materials not in junk:
                junk[materials] = quantity
            else:
                junk[materials] += quantity

        for key, value in significunt.items():
            if value >= 250:
                isObtained = True
                significunt[key] -= 250
                print(f"{key_materials[key]} obtained!")
                break
    if isObtained:
        break

    data = input()

sorted_items = sorted(significunt.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for key, value in sorted_items:
    print(f"{key}: {value}")

sorted_junks = sorted(junk.items(), key=lambda kvp: kvp[0])
for key, value in sorted_junks:
    print(f"{key}: {value}")