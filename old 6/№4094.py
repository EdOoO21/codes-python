for i in range(-100,10000):
    s = i
    n = 12
    while s > 0:
        s = s - 10
        n = n + 7
    if n == 61:
        print(i)