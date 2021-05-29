import sys
number = int(input())
max = -sys.maxsize
max_snow = -sys.maxsize
max_time = -sys.maxsize
max_quality = -sys.maxsize

for snowball in range(1, number +1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if snowball_value > max:
        max = snowball_value
        max_snow = snowball_snow
        max_time = snowball_time
        max_quality = snowball_quality

print(f"{max_snow} : {max_time} = {int(max)} ({max_quality})")