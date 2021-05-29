n = int(input())
even = []
odd = []
positive = []
negative = []

for x in range(n):
    numbers = int(input())
    if numbers % 2 == 0:
        even.append(numbers)
    if numbers % 2 == 1:
        odd.append(numbers)
    if numbers >= 0 :
        positive.append(numbers)
    if numbers < 0:
        negative.append(numbers)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
else:
    print(negative)