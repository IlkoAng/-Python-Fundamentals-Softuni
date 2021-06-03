import re

text = input()
regex = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

numbers = re.finditer(regex, text)

number = [n.group() for n in numbers]
print(*number)