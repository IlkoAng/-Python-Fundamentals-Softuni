import re

usernames = input().split(", ")
allowed = "^[A-Za-z0-9_-]*$"

for name in usernames:
    if 3 < len(name) < 16:
        state = bool(re.match(allowed, name))
        if state is True:
            print(name)


