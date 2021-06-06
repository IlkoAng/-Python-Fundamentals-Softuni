shopping_list = input().split("!")
command = input()
old_item = ""
while not command == "Go Shopping!":
    if "Correct" in command:
        action, old_item, item = command.split()
    else:
        action, item = command.split()

    if action == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)

    elif action == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)

    elif action == "Correct":
        if old_item in shopping_list:
            x = shopping_list.index(old_item)
            shopping_list.pop(x)
            shopping_list.insert(x, item)

    elif action == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)

    command = input()

print(", ".join(shopping_list))
