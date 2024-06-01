f = open('24 (10).txt').readline()

from itertools import *

for i in permutations('SOLO', 4):
    a = i[0] + i[1] + i[2] + i[3]
    f = f.replace(a, '*')

f = f.split('*')

maxlen = 0
lenv = ''
for i in range(len(f) - 4):
    x = f[i] + f[i+1] + f[i+2] + f[i + 3] + f[i + 4]
    x1 = set(x)
    counter = 0
    for k in x1:
        if k in '0123456789':
            counter += 1
    if counter >= 5:
        if len(x) > maxlen:
            maxlen = len(x)
            lenv = x

print(maxlen + 16 + 6,lenv)
