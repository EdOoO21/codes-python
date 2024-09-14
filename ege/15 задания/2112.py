A = 3
ok = True
for x in range(1,1000):
    for y in range(1, 1000):
        for z in range(1, 1000):
            if (((z % 115 == 0) or (y % 78 == 0) or (x % 51 == 0)) <= ((x*y*z) % A == 0)) == 0:
                ok = False
                print(x)
                break
        if not ok:
            print(y)
            break
    if not ok:
        print(z)
        break
if ok:
        print(A)