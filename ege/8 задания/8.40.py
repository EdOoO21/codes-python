l = 'plusenok'
k = 0
p = 'euo'
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        for g in l:
                            w = a + b + d + c + e + f + g
                            flag = 0
                            if a != 'p' and a != 'l' and a != 'input.txt' \
                                    and a != 'n' and a != 'k':
                                for i in range(7):
                                    if (0 < i < 6 and w[i] == 'e' and (w[i + 1] not in p
                                                                       or w[i - 1] not in p)):
                                        flag = 1
                                        break
                                    if i == 0 and w[i] == 'e' and w[i + 1] not in p:
                                        flag = 1
                                        break
                                    if i == 6 and w[i] == 'e' and w[i - 1] not in p:
                                        flag = 1
                                        break
                                if flag == 0:
                                    k += 1
                                    print(w)

print(k)
