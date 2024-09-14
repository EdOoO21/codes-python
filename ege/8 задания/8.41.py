l = 'rosmha'
k = 0
g = 'ao'
s = 'rsmh'
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        for g1 in l:
                            for h in l:
                                w = a + b + c + d + e + f + g1 + h
                                flag = 0
                                if w.count('r') == 1 and w.count('o') == 2 \
                                        and w.count('input.txt') == 1 and w.count('m') == 1 \
                                        and w.count('a') == 2 and w.count('h') == 1:
                                    for i in range(8):
                                        if i == 0 and w[i] in g and w[i + 1] in g:
                                            flag = 1
                                            break
                                        if i == 0 and w[i] in s and w[i + 1] in s:
                                            flag = 1
                                            break
                                        if i == 7 and w[i] in s and w[i - 1] in s:
                                            flag = 1
                                            break
                                        if i == 7 and w[i] in g and w[i - 1] in g:
                                            flag = 1
                                            break
                                        if 0 < i < 7 and w[i] in s \
                                                and (w[i + 1] in s or w[i - 1] in s):
                                            flag = 1
                                            break
                                        if 0 < i < 7 and w[i] in g \
                                                and (w[i + 1] in g or w[i - 1] in g):
                                            flag = 1
                                            break
                                    if flag == 0:
                                        print(w)
                                        k += 1
print(k)
