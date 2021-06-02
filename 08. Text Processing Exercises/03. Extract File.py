text = [word.split(".") for word in input().split("\\") if "." in word]
print(f"File name: {text[0][0]}")
print(f"File extension: {text[0][1]}")