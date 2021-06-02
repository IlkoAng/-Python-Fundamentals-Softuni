word1, word2 = input().split()
sliced = ""
total_sum = 0
if len(word1) > len(word2):
    sliced = word1[len(word2):]
    for idx in range(len(word2)):
        total_sum += ord(word1[idx]) * ord(word2[idx])
    for dig in sliced:
        total_sum += ord(dig)

elif len(word1) < len(word2):
    sliced = word2[len(word1):]
    for idx in range(len(word1)):
        total_sum += ord(word1[idx]) * ord(word2[idx])
    for dig in sliced:
        total_sum += ord(dig)
else:
    for idx in range(len(word1)):
        total_sum += ord(word1[idx]) * ord(word2[idx])
    for dig in sliced:
        total_sum += ord(dig)

print(total_sum)