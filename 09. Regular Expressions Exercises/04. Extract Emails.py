import re

text = input()

regex = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"

valids = [obj.group() for obj in re.finditer(regex, text)]

print("\n".join(valids))

