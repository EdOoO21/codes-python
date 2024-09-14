k = 0
for a in range(1,10000):
    ok = True
    for x in range(1,1000):
        for y in range(1,1000):
            if (((x<5) <= (x**2 < a)) and ((y**2 <= a) <= (y<=5))) == 0:
                ok = False
                break
    if ok:
        print(a)
        k+=1
print(k)