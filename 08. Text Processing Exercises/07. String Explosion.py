text = input().split(">")
new_text = []
boom = 0


for el in text:
    if el.isdigit():
        boom += int(el)
        boom -= 1
    else:
        pass