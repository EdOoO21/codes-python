l = '01234567'
counter = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    w = a+b+c+d+e

                    if a != '0' and w.count('6') == 1 and '61' not in w and '16' not in w \
                        and '63' not in w and '36' not in w and '65' not in w and '56' not in w \
                            and '67' not in w and '76' not in w:
                        print(w)
                        counter += 1

print(counter)