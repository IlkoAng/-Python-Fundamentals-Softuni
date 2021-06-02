command = input()
mydict = {}
counter = 0
word = ""

while not command == "stop":
    counter += 1
    if counter % 2 != 0:
        word = command
        if command not in mydict:
            mydict[word] = 0
    else:
        mydict[word] += int(command)

    command = input()

for key, value in mydict.items():
    print(f"{key} -> {value}")