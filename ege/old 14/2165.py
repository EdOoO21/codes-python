s = 7 ** 103 + 20 * (7 ** 204) - 3 * (7 ** 57) + 97
k = 0
while s>0:
    if s % 7 == 6:
        k+=1
    s//=7
print(k)