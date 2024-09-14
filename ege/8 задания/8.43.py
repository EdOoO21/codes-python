l = 'leonid'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        w = a+b+c+d+e+f
                        if w.count('l') == 2 and w.count('o') >= 1:
                            k+=1
                            print(w)
print(k)