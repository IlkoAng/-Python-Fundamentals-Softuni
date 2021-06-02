command = input()
courses = {}
while not command == "end":
    course, name = command.split(" : ")

    if course not in courses:
        courses[course] = []
    courses[course] += [name]

    command = input()

courses = dict(sorted(courses.items(), key=lambda kvp: -len(kvp[1])))

for key, value in courses.items():
    courses[key].sort()
    print(f"{key}: {len(value)}")
    for names in courses[key]:
        print(f"-- {names}")
