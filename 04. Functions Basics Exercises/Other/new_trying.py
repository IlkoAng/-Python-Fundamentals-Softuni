def exchange(index, fun_list):
    first_part = fun_list[:index+1]
    second_part = fun_list[index+1:]
    fun_list = second_part + first_part
    return fun_list


def max_number(fun_list):
    if not fun_list:
        print("No matches")
    else:
        max = min(fun_list)
        for el in fun_list:
            if el >= max:
                max = el
        index_rightmost_max = len(mylist) - 1 - mylist[::-1].index(max)
        print(index_rightmost_max)


def min_number(fun_list):
    if not fun_list:
        print("No matches")
    else:
        min = max(fun_list)
        for el in fun_list:
            if el <= min:
                min = el
        index_rightmost_min = len(mylist) - 1 - mylist[::-1].index(min)
        print(index_rightmost_min)


def first_needed(fun_list, count):
    if len(mylist) < count:
        print("Invalid count")
    elif len(fun_list) == 0:
        print(fun_list)
    else:
        new = fun_list[:count]
        print(new)


def last_needed(fun_list, count):
    if len(mylist) < count:
        print("Invalid count")
    elif len(fun_list) == 0:
        print(fun_list)
    else:
        fun_list = fun_list[::-1]
        new = fun_list[:count]
        print(list(reversed(new)))


numbers_as_string = input().split()
mylist = list(map(int, numbers_as_string))
command = input()
new = []

while not command == "end":
    action = command.split()

    if action[0] == "exchange":
        idx = action[1]
        idx = int(idx)
        if 0 <= idx < len(mylist):
            mylist = exchange(idx, mylist)
        else:
            print("Invalid index")

    elif action[0] == "max":
        if action[1] == "even":
            even_nums = [x for x in mylist if x % 2 == 0]
            max_number(even_nums)
        elif action[1] == "odd":
            odd_nums = [x for x in mylist if x % 2 != 0]
            max_number(odd_nums)

    elif action[0] == "min":
        if action[1] == "even":
            even_nums = [x for x in mylist if x % 2 == 0]
            min_number(even_nums)
        elif action[1] == "odd":
            odd_nums = [x for x in mylist if x % 2 != 0]
            min_number(odd_nums)

    elif action[0] == "first":
        counter = int(action[1])
        if action[2] == "even":
            even_nums = [x for x in mylist if x % 2 == 0]
            first_needed(even_nums, counter)
        elif action[2] == "odd":
            odd_nums = [x for x in mylist if x % 2 != 0]
            first_needed(odd_nums, counter)
    elif action[0] == "last":
        counter = int(action[1])
        if action[2] == "odd":
            odd_nums = [x for x in mylist if x % 2 != 0]
            last_needed(odd_nums, counter)
        elif action[2] == "even":
            even_nums = [x for x in mylist if x % 2 == 0]
            last_needed(even_nums, counter)
    command = input()

print(mylist)