def check_password(pword):
    is_valid = True
    counter = 0
    if len(pword) < 6 or len(pword) > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not pword.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")

    for el in pword:
        if el.isdigit():
            counter += 1
    if counter < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        print("Password is valid")


password = input()
check_password(password)


