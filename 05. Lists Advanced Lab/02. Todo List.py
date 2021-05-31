command = input()
schedule = [0] * 10

while command != "End":
    notes = command.split("-")
    time = notes[0]
    action = notes[1]
    time = int(time) -1
    schedule[time] = action
    #schedule.insert(time, action)

    command = input()

print([action for action in schedule if action != 0])