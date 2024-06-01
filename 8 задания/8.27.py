l = 'timofey'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        w = a+b+c+d+e+f

                        if a != 'y' and f != 'y' and w.count('y') <= 1\
                            and w.count('iy') == 0 and w.count('yi') == 0:
                            k+=1
                            print(w)
print(k)


