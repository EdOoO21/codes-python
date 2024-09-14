for a in range(1, 10000):
    ok = True
    for y in range(1, 1000):
        for x in range(1, 1000):
            if ((y >= a) or (x > a) or (x * y < 130)  )== 0:
                ok = False
                break
    if ok:
        print(a)
        

