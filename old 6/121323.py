for i in range(-1000,1000):
    s = i
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if n == 64:
        print(i)
        break
