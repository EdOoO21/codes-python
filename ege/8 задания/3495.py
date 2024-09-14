s = 'пскаль'
k = 0
l = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                w = a+b+c+d
                if a!='ь' and ((b == 'ь' and c != 'ь') or (b != 'ь' and c == 'ь' and d != 'ь') or (d == 'ь' and c != 'ь') or (b != 'ь' and c != 'ь' and d != 'ь')):
                    print(w)
                    k+=1
                if w.count('ь') == 1 and a != 'ь':
                    l+=1
                    print(w)
                elif w.count('ь') == 2 and a != 'ь' and (b == 'ь' and d == 'ь'):
                    l += 1
                    print(w)
                elif (d != 'ь' and b != 'ь') and w.count('ь') == 2 and a != 'ь':
                    l += 1
                    print(w)
                elif w.count('ь') != 3 and w.count('ь') != 4 and w.count('ь') != 2 and w.count('ь') != 1 and a != 'ь':
                    l+=1
                    print(w)
print(k,l)