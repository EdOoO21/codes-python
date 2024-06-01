from itertools import permutations
from functools import reduce

l = str(input())
l = sorted(l)
l1 = str(reduce(lambda x, y: x + y, l))
for i in permutations(l1, len(l)):
    print(''.join(i))
