start = int(input())
stop = int(input())
final = ""

for num in range(start, stop +1):
    final += chr(num)
    final += " "
print(final)