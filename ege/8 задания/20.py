l = 'тимофей'
counter = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    w = a +b+c+d+e
                    if w.count('й')<=1 and a != 'й' and e != 'й' and 'ий' not in w and 'йи' not in w:
                        print(w)
                        counter += 1
print(counter)

