factor = int(input())
count = int(input())
my_list = []
counter = 0
while len(my_list) < count:
    counter += 1
    if counter % factor == 0:
        my_list.append(counter)

print(my_list)
