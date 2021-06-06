numbers = [int(num) for num in input().split()]
isEnough = True
average = sum(numbers) / len(numbers)

filtered = [num for num in numbers if num > average]

#filtered.reverse()

if len(filtered) > 5:
    while len(filtered) > 5:
        filtered.pop(0)

if len(numbers) < 5:
    print("No")
    isEnough = False


filtered.sort(reverse=True)

filtered = [str(num) for num in filtered]
if isEnough:
    print(" ".join(filtered))

