substrings = input().split(", ")
strings = input().split(", ")
my_list = []

for substring in substrings:
    for string in strings:
        if substring in string:
            my_list.append(substring)

print(sorted(set(my_list), key=my_list.index))