y = 7**103 - 6 * 7**70 + 3 * 7**57 - 98
count = 0
while y > 0:
    if y % 7 == 6:
        count+=1
    y //=7
print(count)
