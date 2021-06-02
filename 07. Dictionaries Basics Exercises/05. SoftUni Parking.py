number = int(input())
registered = {}
unregistered = {}

for num in range(number):
    command = input().split()

    if command[0] == "register":
        username = command[1]
        license_number = command[2]
        if username not in registered:
            registered[username] = license_number
            print(f"{username} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    else:
        username = command[1]
        if username in registered:
            del registered[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for key, value in registered.items():
    print(f"{key} => {value}")



