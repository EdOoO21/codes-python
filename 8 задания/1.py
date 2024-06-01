l = '01234567'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    w = a+b+c+d+e
                    if w.count('4') == 2 and ('24' not in w)\
                        and ('42' not in w) and ('44' not in w)\
                        and ('64' not in w) and ('46' not in w)\
                        and ('04' not in w) and ('40' not in w) and a != '0':
                        print(w)
                        k+=1
print(k)