def ascii_code(start, stop):
    start_char = ord(start)
    stop_char = ord(stop)
    my_list = []
    for idx in range(start_char + 1, stop_char):
        el = chr(idx)
        my_list.append(el)
    return my_list


char1 = input()
char2 = input()
print(" ".join(ascii_code(char1, char2)))