for a in range(10):
    for b in range(10):
        s = '1263' + str(a) + '5' + str(b)
        if int(s) % 3123 == 0:
            print(s)

for a in range(10):
    for b in range(10):
        for c in range(10):
            s = '12' + str(a) + '63' + str(b) + '5' + str(c)
            if int(s) % 3123 == 0:
                print(s)

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                s = '12' + str(a) + str(b) + '63' + str(c) + '5' + str(d)
                if int(s) % 3123 == 0:
                    print(s)