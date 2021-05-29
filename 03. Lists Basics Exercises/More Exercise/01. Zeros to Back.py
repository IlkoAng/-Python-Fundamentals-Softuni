
my_list = input().split(", ")



for num in my_list:
    if num == "0":
        my_list.remove(num)
        my_list.append(num)
    else:
        continue
my_list = [int(num) for num in my_list]
print(my_list)