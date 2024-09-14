l = 'аелмнорь'
counter = 1
fl = 0
m = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        w = a + b + c + d + e + f
                        if w == 'ненорм':
                            fl = 1
                            print(counter, w)


                        if fl == 1 and w != 'ненорм':
                            print(counter, w)
                            m += 1
                        if w[:4] == 'норм':
                            fl = 2

                        counter += 1
                    if fl == 2:
                        break
                if fl == 2:
                    break
            if fl == 2:
                break
        if fl == 2:
            break
    if fl == 2:
        break
print(m)
