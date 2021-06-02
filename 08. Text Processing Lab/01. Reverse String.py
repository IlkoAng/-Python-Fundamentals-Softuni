command = input()

while not command == "end":
    res = ""

    for index in range(len(command)-1, -1, -1):
        res += command[index]
    print(f"{command} = {res}")
    command = input()