number_wagons = int(input())
wagons = [0] * number_wagons

command = input()

while command != "End":
    data = command.split()
    if data[0] == "add":
        wagons[-1] += int(data[1])
    elif data[0] == "insert":
        idx = data[1]
        idx = int(idx)
        people = data[2]
        people = int(people)
        wagons[idx] += people
    elif data[0] == "leave":
        idx = data[1]
        idx = int(idx)
        people = data[2]
        people = int(people)
        wagons[idx] -= people

    command = input()

print(wagons)
