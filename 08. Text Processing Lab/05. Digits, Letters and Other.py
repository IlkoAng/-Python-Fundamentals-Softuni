text = input()
digits = ""
letters = ""
others = ""

for letter in text:
    if letter.isdigit():
        digits += letter
    elif letter.isalpha():
        letters += letter
    else:
        others += letter

print(digits)
print(letters)
print(others)
