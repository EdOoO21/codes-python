l = 'rosomaha'
from itertools import *
counter = 0
s = 'ao'
for i in set(permutations(l,8)):
    if (i[0] in s and i[1] not in s and i[2] in s and i[3] not in s and i[4] in s and i[5] not in s and i[6] in s and i[7] not in s)\
            or (i[0] not in s and i[1] in s and i[2] not in s and i[3] in s and i[4] not in s and i[5] in s and i[6] not in s and i[7] in s):
        counter+=1
        print(i)

print(counter)