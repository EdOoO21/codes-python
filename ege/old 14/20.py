s = 343 ** 5 - 7 ** 9 + 48
c = 0
while s > 0:
    if s % 7 == 6:
        c += 1

    s //= 7
print(c)
