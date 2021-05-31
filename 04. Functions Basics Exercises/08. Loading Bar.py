def loading_bar(number):
    bar = ["."] * 10
    number /= 10

    if number == 0:
        return bar

    for idx in range(int(number)):
        bar[idx] = "%"
    return bar


num = int(input())
bar_result = loading_bar(num)

if bar_result.count("%") == 10:
    print("100% Complete!")
    print(f"[{''.join(bar_result)}]")

else:
    print(f"{num}% [{''.join(bar_result)}]")
    print("Still loading...")