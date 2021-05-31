numbers = input().split(", ")
boundary = 10
numbers = [int(x) for x in numbers]
max_num = max(numbers)
while numbers:
    my_list = []
    for num in numbers:
        if num in range(boundary - 10, boundary+1):
            my_list.append(num)

    for nums in my_list:
        numbers.remove(nums)
    print(f"Group of {boundary}'s: {my_list}")
    boundary += 10
