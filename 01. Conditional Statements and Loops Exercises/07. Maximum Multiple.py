import sys
divisor = int(input())
bound = int(input())
max = -sys.maxsize

for n in range(divisor, bound + 1):
    if n % divisor == 0 and n <= bound:
        max = n
print(max)
