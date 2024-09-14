l = 'polygn'
counter = 0
for a in l:
    for b in l:
        for c in 'o':
            for d in l:
                for e in l:
                    w = a+b+c+d+e
                    if w[2] == 'o' and w[0]==w[4] and w[1] == w[3]:
                        print(w)
                        counter += 1
print(counter)