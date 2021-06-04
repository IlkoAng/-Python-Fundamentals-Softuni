import re

text = input()

regex = r"www.[A-Za-z0-9-]+(\.[a-z]+)+"

while text:

    valids = [obj.group() for obj in re.finditer(regex, text)]
    if valids:
        print("\n".join(valids))

    text = input()


