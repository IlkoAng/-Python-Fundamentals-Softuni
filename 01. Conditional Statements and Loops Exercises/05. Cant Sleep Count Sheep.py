number = int(input())
counter = ""
for x in range(1, number +1):
    counter += str(x)
    counter += (f" sheep...")
print(counter)