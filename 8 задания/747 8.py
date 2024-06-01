l = 'aekrt'
counter = 1
f = 0
s = [0,0]
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    for f in l:
                        w = a+b+c+d+e+f
                        if w == 'kareta':
                            s[0] = counter
                        if w == 'raketa':
                            s[1] = counter

                        counter += 1
print(s[1] - s[0]-1)



from itertools import *
l = 'аекрт'
kareta = 0
raketa = 0
counter = 0
for i in product(l, repeat=6):
    a = ''.join(i)
    counter += 1
    if a == 'карета':
        kareta = counter
    if a == 'ракета':
        raketa = counter

print(abs(kareta - raketa)-1)
