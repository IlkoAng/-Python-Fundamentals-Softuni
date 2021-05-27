word = input()
reversed = ""
for char in range(len(word) -1, -1, -1):
    reversed += word[char]
print(reversed)