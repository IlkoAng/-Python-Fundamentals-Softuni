import re

text = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

my_list = re.findall(pattern, text)

print(" ".join(my_list))