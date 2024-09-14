s = 'uley'
k = 0

for a in s:
    for b in s:
        for c in s:
            for d in s:
                w = a+b+c+d
                if w.count('u')==1 and w.count('l')==1 and w.count('e')==1 and w.count('y')==1\
                    and a!='y' and w.count('eu')==0:
                    print(w)
                    k+=1
print(k)