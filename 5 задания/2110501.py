for i in range(10, 100000):
    s = []
    l = str(i)
    for n in range(len(l) - 1):
        s.append(int(l[n] + l[n + 1]))

    if (max(s) - min(s)) == 44:
        print(i, s)
        break