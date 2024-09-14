f = [0] * ((9 ** 9) + 10)
counter = 0
for i in range(0, ((9 ** 9) + 10)):
    if i < 9:
        f[i] = (i // 3) + (i % 3)
    if i >= 9:
        f[i] = f[i // 9] + f[i % 9]
        if 0 <= i < 9 ** 9 and f[i] == 33:
            counter += 1

print(counter)
