n = int(input())

positive = []
negative = []

for _ in range(n):
    number = int(input())
    if number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)
print(positive)
print(negative)
print(f"Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}")