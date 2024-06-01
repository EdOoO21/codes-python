c = []
for x in range(30,46):
    c += [x]

for a in range(1,10000):
    ok = True
    for x in range(1,10000):
        if (((x % a == 0) and (x in c)) <= (not(x % 12 == 0))) == 0:
            ok = False
            break
    if ok:
        print(a)
        break