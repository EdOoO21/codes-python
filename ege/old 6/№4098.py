for i in range(-100,10000):
    s = i
    n = 20
    while n > s:
        s = s + 1
        n = n - 1
    if n == 16:
        print(i)
        break