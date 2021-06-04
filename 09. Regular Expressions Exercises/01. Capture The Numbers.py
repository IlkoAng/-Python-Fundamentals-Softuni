import re

text = input()
regex = r"\d+"
mylist = []

while text:
    valids = re.findall(regex, text)
    mylist.extend(valids)
    text = input()

print(*mylist)