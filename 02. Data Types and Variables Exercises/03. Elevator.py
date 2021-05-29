number = int(input())
capacity = int(input())
course = 0

while number > 0:
    number -= capacity
    course += 1

print(course)