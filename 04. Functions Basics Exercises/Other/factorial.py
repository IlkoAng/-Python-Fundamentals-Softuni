import sys
numbers_as_string = input().split()
mylist = list(map(int, numbers_as_string))
command = input()
max = -sys.maxsize
min = sys.maxsize
new = []
isValid = False
while not command == "end":
    action = command.split()

    if action[0] == "exchange":
        idx = action[1]
        idx = int(idx)
        if 0 <= idx < len(mylist):
            first = mylist[:idx+1]
            second = mylist[idx+1:]
            mylist = second + first
        else:
            print("Invalid index")
    elif action[0] == "max":
        if action[1] == "even":
            for el in mylist:
                if el % 2 == 0 and el > max:
                    max = el
                    isValid = True
                if isValid:
                    print(mylist.index(max))
                if not isValid:
                    print("No matches")
        elif action[1] == "odd":
            for el in mylist:
                if el % 2 != 0 and el > max:
                    max = el
                    isValid = True
                if isValid:
                    print(mylist.index(max))
                if not isValid:
                    print("No matches")

    elif action[0] == "min":
        if action[1] == "even":
            for el in mylist:
                if el % 2 == 0 and el <= min:
                    min = el
                    isValid = True
                if isValid:
                    print(mylist.index(min))
                if not isValid:
                    print("No matches")
        elif action[1] == "odd":
            for el in mylist:
                if el % 2 != 0 and el <= min:
                    min = el
                    isValid = True
                if isValid:
                    print(mylist.index(min))
                if not isValid:
                    print("No matches")
    elif action[0] == "first":
        if action[2] == "even":
            number = action[1]
            number = int(number)
            for el in mylist:
                if el % 2 == 0:
                    new.append(el)
                    if len(new) == number:
                        break
        elif action[2] == "odd":
            number = action[1]
            number = int(number)
            for el in mylist:
                if el % 2 != 0:
                    new.append(el)
                    if len(new) == number:
                        break
    elif action[0] == "last":
        pass
    isValid = False
    command = input()