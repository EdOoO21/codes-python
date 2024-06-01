for i in range(-10000,10000):
    s = i
    n = 10
    while s - n < 1000:
        s += n
        n += 5
    if n == 80:
        print(i)

