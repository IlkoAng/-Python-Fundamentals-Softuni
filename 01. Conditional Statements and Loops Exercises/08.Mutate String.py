str_1 = input()
str_2 = input()
new = ""
previous = str_1
for idx in range(len(str_1)):
    for x in range(0, idx +1):
        new += str_2[x]
    for y in range(idx +1, len(str_2)):
        new += str_1[y]
    if not new == previous:
        print(new)
    previous = new
    new = ""