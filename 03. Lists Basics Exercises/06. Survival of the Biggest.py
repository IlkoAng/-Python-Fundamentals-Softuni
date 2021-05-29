import sys
my_list = input().split(" ")
number = int(input())
min = sys.maxsize
new = []
for x in range(number):
    for elm in my_list:
        if int(elm) < int(min):
            min = elm
    my_list.remove(min)
    min = sys.maxsize
for elm in my_list:
    new.append(int(elm))
print(new)