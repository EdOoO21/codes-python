for i in range(-100,10000):
    s = i
    n = 600
    while n > s:
        s = s + 3
        n = n - 6
    if n == 210:
        print(i)