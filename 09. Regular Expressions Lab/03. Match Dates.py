import re
text = input()
regex = r"(?P<Day>\d{2})(?P<separator>[\.\-\/])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})"

valid = [el.groupdict() for el in re.finditer(regex, text)]

print('\n'.join([f"Day: {date['Day']}, Month: {date['Month']}, Year: {date['Year']}" for date in valid]))

