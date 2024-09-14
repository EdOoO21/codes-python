for i in range(-100,10000):
    s = i
    n = 1
    while s < 28:
        s = s + 5
        n = n * 3
    if n == 81:
        print(i)