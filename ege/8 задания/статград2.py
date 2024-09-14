l = 'парабола'
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
                                if word.count('п') == 1 and word.count('о') == 1 \
                                 and word.count('р') == 1 and word.count('б') == 1 \
                                 and word.count('а') == 3 and word.count('л') == 1 \
                                 and word.count('ао') == 0 and word.count('оа') == 0 \
                                 and word.count('пр') == 0 and word.count('рп') == 0 \
                                 and word.count('рб') == 0 and word.count('бр') == 0 \
                                 and word.count('пб') == 0 and word.count('бп') == 0 \
                                 and word.count('бл') == 0 and word.count('лб') == 0 \
                                 and word.count('рл') == 0 and word.count('лр') == 0 \
                                 and word.count('пл') == 0 and word.count('лп') == 0 \
                                 and word.count('аа') == 0:
                                     k += 1
                                     print(word)
print(k)
