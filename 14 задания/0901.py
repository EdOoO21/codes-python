for x in range(15):
    a = 8 * (16**4) + 5 * (16**3) + 6 * (16**2) + 9 * 16 + x
    b = 1 * (16**4) + 2 * (16**3) + x * (16**2) + 4 * 16 + 8
    c = oct(a + b)[2:]
    counter = 0
    ok = True
    for i in range(len(c)):
        if int(c[i]) % 2 == 0:
            counter += 1
        if counter > 2:
            ok = False
            break
    if ok:
        print(x,c)
    
