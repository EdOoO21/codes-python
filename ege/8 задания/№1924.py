l = 'voron'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    w = a + b + c + d + e
                    if w.count('v') == 1 and w.count('r') == 1 \
                            and w.count('n') == 1 and w.count('o') == 2 \
                            and a != b and b != c and c != d and d != e:
                        print(w)
                        k += 1
print(k)