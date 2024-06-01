l = '1234567890'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        w = a+b+c+d+e+f
                        if a != '0' and w.count('1') <= 1 \
                            and w.count('2') <= 1 \
                            and  w.count('3') <= 1 \
                                and w.count('4') <= 1 \
                                and w.count('5') <= 1 \
                                and w.count('6') <= 1 \
                                and w.count('7') <= 1 \
                                and w.count('8') <= 1 \
                                and w.count('9') <= 1 \
                                and w.count('0') <= 1 :
                            if (int(a) % 2 == 0 and int(b) % 2 == 1\
                                and int(c) % 2 == 0 and int(d) % 2 == 1\
                                and int(e) % 2 == 0 and int(f) % 2 == 1) \
                                or (int(a) % 2 == 1 and int(b) % 2 == 0\
                                and int(c) % 2 == 1 and int(d) % 2 == 0\
                                and int(e) % 2 == 1 and int(f) % 2 == 0):
                                k+=1
                                print(w)
print(k)
