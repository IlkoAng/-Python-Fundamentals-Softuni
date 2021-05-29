number = int(input())
total = 0
for num in range(1, number +1):
    letter = input()
    total += ord(letter)

print(f"The sum equals: {total}")