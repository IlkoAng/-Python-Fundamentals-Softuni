text = input()
idx = 0
new = ""
while idx < len(text)-1:
    if text[idx] == text[idx+1]:
        replaced = f"{text[idx]}{text[idx+1]}"
        text = text.replace(replaced, text[idx])
        idx = 0
    else:
        idx += 1
print(text)