l='0123456789'
l1 = '1'
counter = 0
for a in l1:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        for g in l:
                            for h in l:
                                for i in l:
                                    w = a+b+c+d+e+f+g+h+i
                                    if len(set(w)) >= 3:
                                        print(w)
                                        counter += 1

print(counter)

