l = '0123456'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        for g in l:
                            flag = 0
                            w = a + b + c + d + e + f + g
                            if a != '0' and a != '3' and a != '5':
                                if '22' in w and '44' in w:
                                    flag = 1
                                if flag == 0:
                                    print(w)
                                    k += 1
print(k)
