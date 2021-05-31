number = int(input())
free_chairs = 0
isEnough = True
for num in range(1, number+1):
    room = input().split()
    chairs = room[0]
    people = int(room[1])
    diff = abs(len(chairs) - people)
    if len(chairs) > people:
        free_chairs += len(chairs) - people
    elif len(chairs) < people:
        print(f"{diff} more chairs needed in room {num}")
        isEnough = False
if isEnough:
    print(f"Game On, {free_chairs} free chairs left")