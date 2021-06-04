import re
text = input()
searched = input()
regex = fr"\b{searched}\b"
valids = re.findall(regex, text, re.IGNORECASE)

print(len(valids))