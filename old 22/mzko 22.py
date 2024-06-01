for i in range(10000):
    x = i
    L = 0
    M = 0
    while x > 0:
        L = L+1
        if M < (x % 8):
            M = x % 8
        x = x // 8
    if L == 4 and M == 7:
        print(i)
