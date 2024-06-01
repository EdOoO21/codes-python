l = 'acgt'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    w = a+b+c+d+e
                    if w.count('a')==2:
                        print(w)
                        k+=1
print(k)
