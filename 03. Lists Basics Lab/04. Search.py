n = int(input())
word = input()
my_list = []

for i in range(n):
    strings = input()
    my_list.append(strings)
print(my_list)

for idx in range(len(my_list) -1, -1, -1):
    element = my_list[idx]
    if word not in element:
        my_list.remove(element)
print(my_list)



