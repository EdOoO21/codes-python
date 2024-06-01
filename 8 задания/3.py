l = 'knorsa'
counter = 1
ok = 1
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        w = a+b+c+d+e+f
                        if w.count('k') <= 3 and w.count('a') == 2:
                            print(w,counter)
                            ok = 0
                            break
                        else:
                            print(w,counter)
                            counter += 1
                    if ok == 0:
                        break
                if ok == 0:
                    break
            if ok == 0:
                break
        if ok == 0:
            break
    if ok == 0:
        break