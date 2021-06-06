people = int(input())
lift = [int(num) for num in input().split()]
isEnough = False

while people > 0:

    for idx in range(len(lift)):
        if int(lift[idx]) < 4:
            needed = 4 - int(lift[idx])
            if people >= needed:
                lift[idx] += needed
                people -= needed
            else:
                lift[idx] += people
                people = 0
                isEnough = True
                break
    break

lift = [str(num) for num in lift]
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    #print(f"{' '.join(lift)}")
    #break

if isEnough:
    print(f"The lift has empty spots!")
    print(f"{' '.join(lift)}")
else:
    print(f"{' '.join(lift)}")
