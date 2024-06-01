l = '1234'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    w = a+b+c+d+e
                    if a!=c and b!=d and c!=e and a != '1':
                        print(w)
                        k+=1
print(k)