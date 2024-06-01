for i in range(1000000,2000001):
    s = 0
    ok = False
    for n in range(1,round(i**0.5)+1):
        if i % n == 0:
            if abs(i/n - n) <= 100:
                s += 1
        if s >= 3:
            ok = True
            break
    if ok:
        print(i)
