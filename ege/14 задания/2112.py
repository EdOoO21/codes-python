s = []
for x in range(8):
    for y in range(8):
        a = 3 * (8**4) + 6 * (8**3) + x * (8**2) + 5 * 8 + 3
        b = 4 * (8 ** 2) + y * 8 + 3
        if (a - b) > 0 :
            s.append((a - b))
print(min(s))
