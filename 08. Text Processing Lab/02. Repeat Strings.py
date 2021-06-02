text = input().split()
concant = ""
for word in text:
    for n in range(len(word)):
        concant += word
print(concant)