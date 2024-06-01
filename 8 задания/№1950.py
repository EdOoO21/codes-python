l = 'бак'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                w = a+b+c+d
                if a!=b and b!=c and c!=d and w.count('к') == 1\
                        and w.count('а') == 2 and w.count('б') == 1:
                    print(w)
                    k+=1
print(k)