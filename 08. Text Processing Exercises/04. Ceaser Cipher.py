text = input()
as_number = 0
new = ""
for let in text:
    as_number = (ord(let) +3)
    new += chr(as_number)
print(new)