import re

phone = input()
regex = r"\+359( |-)2\1\d{3}\1\d{4}\b"

valid_number = [obj.group() for obj in re.finditer(regex, phone)]
print(", ".join(valid_number))