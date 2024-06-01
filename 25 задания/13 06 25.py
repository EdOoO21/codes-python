def razl(x):
    p = 1
    i = 2
    s = []
    x1 = x
    while p != x1:
        if x % i == 0:
            p *= i
            s.append(i)
            x //= i
        else:
            i += 1

    return s

from fnmatch import *
for i in range(1,10001):
    k = razl(i)
    if len(k) == 7 and fnmatch(str(i),'*2?2'):
        print(i,k[-1])


