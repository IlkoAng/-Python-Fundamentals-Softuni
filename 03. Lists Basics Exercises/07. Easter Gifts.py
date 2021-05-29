gifts = input().split(" ")
command = input()

while command != "No Money":
    current_gift = command.split()
    if current_gift[0] == "OutOfStock":
        for idx in range(len(gifts)):
            if current_gift[1] == gifts[idx]:
                gifts[idx] = "None"

    elif current_gift[0] == "Required":
        index = int(current_gift[2])
        if 0 <= index < len(gifts):
            gifts[index] = current_gift[1]

    elif current_gift[0] == "JustInCase":
        gifts[-1] = current_gift[1]
    command = input()

for elm in gifts:
      if elm != "None":
        print(elm, end=" ")