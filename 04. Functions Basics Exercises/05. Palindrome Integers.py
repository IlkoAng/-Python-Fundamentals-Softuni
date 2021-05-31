def palindrome(numbers):
    rev = " "

    for elem in numbers:
        rev = elem[::-1]
        if elem == rev:
            print("True")
        else:
            print("False")


nums = input().split(", ")
palindrome(nums)
