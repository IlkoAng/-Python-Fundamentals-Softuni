def perfect_num(num):
    my_list = []
    for x in range(1, num):
        if num % x == 0:
            my_list.append(x)
    if sum(my_list) == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_num(number)
