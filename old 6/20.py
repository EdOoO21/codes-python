for i in range(1, 10000):
    s = i
    n = 36
    while s < 2020:
        s = s * 2
        n = n + 3
    if n == 60:
        print(i)
        break
