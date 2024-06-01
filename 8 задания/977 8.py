l = 'лмсыь'
counter = 1
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    w = a+b+c+d+e
                    if a == b == 'ы':
                        print(counter, w,' ========================= ')
                    
                    counter += 1