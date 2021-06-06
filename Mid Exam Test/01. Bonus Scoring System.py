from math import ceil
import sys

num_students = int(input())
num_lectures = int(input())
bonus = int(input())
max = -sys.maxsize
max_attend = -sys.maxsize

for stud in range(num_students):
    attend = int(input())
    max_bonus = attend / num_lectures * (5 + bonus)

    if max_bonus > max:
        max = max_bonus
    if attend > max_attend:
        max_attend = attend

print(f"Max Bonus: {ceil(max)}.")
print(f"The student has attended {max_attend} lectures.")