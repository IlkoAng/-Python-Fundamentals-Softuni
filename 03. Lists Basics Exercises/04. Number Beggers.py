money = input().split(", ")
number = int(input())

my_list = []
beggar_start = 0
counter = 0

for beggar in range(1, number +1):

    for idx in range(beggar_start, len(money), number):
        counter += int(money[idx])
    beggar_start += 1
    my_list.append(counter)
    counter = 0

print(my_list)
