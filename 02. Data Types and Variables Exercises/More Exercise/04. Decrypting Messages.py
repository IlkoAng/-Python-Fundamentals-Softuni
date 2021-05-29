add = int(input())
number = int(input())
decrypted = ""

for x in range(number):
    letter = input()
    crypted = ord(letter)
    crypted += add
    decrypted += (f"{chr(crypted)}")
print(decrypted)