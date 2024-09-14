l = '0123456'
counter = 0
for a in '123456':
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in '456':
                        w = a+b+c+d+e+f
                        if (w.count('0') + w.count('2') + w.count('4') + w.count('6')) == 3:
                            counter += 1
                            print(w)

print(counter)
