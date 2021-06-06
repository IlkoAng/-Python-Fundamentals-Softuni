receptionist_one = int(input())
receptionist_two = int(input())
receptionist_three = int(input())
clients = int(input())
hours = 0
rest = 0

total = receptionist_one + receptionist_two + receptionist_three

while clients > total:
    clients -= total
    hours += 1

    if hours % 3 == 0:
        rest += 1


if clients > 0:
    hours += 1

hours += rest

print(f"Time needed: {hours}h.")