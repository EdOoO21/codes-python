'''
l = '012345678'
n = '12345678'
c1 = '02468'
counter = 0
for a in n:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        for g in l:
                            w = a+b+c+d+e+f+g
                            if a != '0' and a in c1 and w.count('8') == 1 and g not in c1:
                                counter += 1
                                print(w)
print(counter)
'''
counter = 0
n2 = '2468'

n3 = '1357'
l = '012345678'
for a in n2:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        for g in n3:
                            w = a+b+c+d+e+f+g
                            if w.count('8') == 1:
                                print(w)
                                counter += 1
print(counter)


