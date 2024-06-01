s = (243**540) - 6 * (9**530) + 21 * (3 ** 511) - 3 * (3**70) - 200
counter = 0
while s > 0:
    if s % 9 == 8:
        counter += 1

    s //= 9

print(counter)