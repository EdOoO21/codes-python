l = 'geraklit'
counter = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        w = a+b+c+d+e+f
                        if w.count(a) == 1 and w.count(b) == 1 and w.count(c) == 1\
                            and w.count(d) == 1 and w.count(e) == 1 and w.count(f) == 1\
                            and (w.count('i') + w.count('a') + w.count('e')) < 3 \
                            and 'ia' not in w and 'ai' not in w and 'ie' not in w \
                                and 'ei' not in w and 'ae' not in w and 'ea' not in w:
                            counter += 1
                            print(w)

print(counter)
