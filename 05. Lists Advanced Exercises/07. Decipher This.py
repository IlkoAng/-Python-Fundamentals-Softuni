secret = input().split()
my_list = []

for word in secret:
    concat = ""
    alpha = []
    x = ""
    y = ""
    for dig in word:
        if dig.isdigit():
            concat += (f"{dig}")
        else:
            alpha.append(dig)
    x = alpha.pop(0)
    if len(alpha) >= 1:
        y = alpha.pop(-1)
    my_list.append(chr(int(concat)))
    my_list.append(y)
    for el in alpha:
        #if el in my_list:
            #continue
        my_list.append(el)
    my_list.append(x)
    my_list.append(" ")
print("".join(my_list))


