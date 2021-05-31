numbers_as_string = input().split(", ")
numbers = [int(num) for num in numbers_as_string]

print([idx for idx in range(len(numbers)) if numbers[idx] % 2 == 0])