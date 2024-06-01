for i in range(-1000,1000):
    s = i
    n = 2
    while s < 37:
        s = s + 3
        n = n * 2
    if n == 128:
        print(i)
