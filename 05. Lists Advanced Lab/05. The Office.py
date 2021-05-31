employees = input().split()
factor = int(input())

my_list = [int(emp)*factor for emp in employees]
average = sum(my_list) / len(employees)
my_list = [el for el in my_list if el >= average]
counter = 0
for el in my_list:
    counter += 1


if counter < len(employees) /2:
    print(f"Score: {counter}/{len(employees)}. Employees are not happy!")
elif counter >= len(employees) /2:
    print(f"Score: {counter}/{len(employees)}. Employees are happy!")
