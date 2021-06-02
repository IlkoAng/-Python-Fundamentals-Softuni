number = int(input())
students = {}

for stud in range(number):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = [grade]
    else:
        students[name] += [grade]

filtered_stud = {}
for key, value in students.items():
    average = sum(value) / len(value)
    if average >= 4.5:
        filtered_stud[key] = average

sorted_stud = sorted(filtered_stud.items(), key=lambda kvp: -kvp[1])

for key, value in sorted_stud:
    print(f"{key} -> {value:.2f}")