def f(x, y, p):
    if x + y >= 30 and p == 3:
        return 1
    if (x + y < 30 and p == 3) or (x + y >= 30 and p != 3):
        return 0
    if p % 2 == 0:
        return any([f(x + 1, y, p + 1), f(x, y + 1, p + 1), f(x * 2, y, p + 1), f(x, y * 3, p + 1)])
    else:
        return all([f(x + 1, y, p + 1), f(x, y + 1, p + 1), f(x * 2, y, p + 1), f(x, y * 3, p + 1)])


counter = 0
for k in range(1, 30):
    for s in range(1, 30):
        if k + s > 29:
            break
        else:
            if f(k, s, 1):
                print(k, s)
                counter += 1

print(counter)
