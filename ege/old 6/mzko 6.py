for i in range(-100,1001):
    s = i
    n = 200
    while s > 0:
        s = s // 4
        n = n - 6
    if n == 170:
        print(i)
