for n in range(13,1000000):
    i = bin(n)[2:]
    for p in range(2):
        s = 0
        for h in i:
            s += int(h)
        if n % 2 == 1 and s % 2 == 1:
            i = i + '1'
        if n % 2 == 0 or s % 2 == 0:
            i = i + bin(s % 2)[2:]

    if int(i,2) < 100:
        print(n)