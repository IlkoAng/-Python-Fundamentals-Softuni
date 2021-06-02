collection = input()
chars = {}
word = collection.split()
for char in word:
    for dig in char:
        if dig not in chars:
            chars[dig] = 0
        chars[dig] += 1

for key, value in chars.items():
    print(f"{key} -> {value}")