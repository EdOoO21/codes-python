l = 'николай'
counter = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        for g in l:
                            for h in l:
                                for i in l:
                                    for j in l:
                                        for k in l:
                                            w = a+b+c+d+e+f+g+h+i+j+k
                                            if a != 'й' and w.count('и') == 1 and w.count('о') == 1 and w.count('а') == 1:
                                                counter += 1
                                                print(w)
print(k)
