l = 'экзамен'
counter = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        for g in l:
                            for h in l:
                                w = a + b + c + d + e + f + g + h
                                if d != e and \
                                        ((w.count('э') + w.count('а') + w.count('е')) == 3 or
                                         (w.count('э') + w.count('а') + w.count('е')) == 5):
                                    counter += 1

print(counter)
