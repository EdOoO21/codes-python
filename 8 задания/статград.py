l = 'росомаха'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        for g in l:
                            for h in l:
                                 word = a + b + c + d + e + f + g + h
                                 if word.count('р') == 1 and word.count('о') == 2 \
                                 and word.count('с') == 1 and word.count('м') == 1 \
                                 and word.count('а') == 2 and word.count('х') == 1 \
                                 and word.count('ао') == 0 and word.count('оа') == 0 \
                                 and word.count('рс') == 0 and word.count('ср') == 0 \
                                 and word.count('см') == 0 and word.count('мс') == 0 \
                                 and word.count('мр') == 0 and word.count('рм') == 0 \
                                 and word.count('мх') == 0 and word.count('хм') == 0 \
                                 and word.count('сх') == 0 and word.count('хс') == 0 \
                                 and word.count('рх') == 0 and word.count('хр') == 0 \
                                 and word.count('оо') == 0 and word.count('аа') == 0:
                                     k += 1
                                     print(word)
print(k)