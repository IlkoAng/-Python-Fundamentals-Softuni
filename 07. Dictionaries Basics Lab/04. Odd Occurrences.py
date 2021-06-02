words = input().split()
mydict = {}

for word in words:
    word_lower = word.lower()

    if word_lower not in mydict:
        mydict[word_lower] = 0
    mydict[word_lower] += 1

for key, value in mydict.items():
    if value % 2 != 0:
        print(key, end=" ")
