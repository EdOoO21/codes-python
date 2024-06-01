l = 'vekno'
k = 1
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    w = a+b+c+d+e
                    if w.count('n') == 2 and w.count('k') == 2:
                        print(k,w,'======================================')
                        k+=1
                    else:
                        print(k,w)
                        k+=1