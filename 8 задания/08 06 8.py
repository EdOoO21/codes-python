l = 'аекнс'
counter = 1
f = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        w = a + b + c + d + e + f
                        print(counter,w)
                        counter += 1
                        if w == 'сенека':
                            f = 1
                            break
                    if f == 1:
                        break
                if f == 1:
                    break
            if f == 1:
                break
        if f == 1:
            break
    if f == 1:
        break