l='azns'
f = 0
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    w = a+b+c+d+e
                    if w == 'sazan':
                        f = 0
                        k+=1
                    if w == 'zanas':
                        f = 1
                    if f == 1:
                        k +=1

                    print(w)
print(k)