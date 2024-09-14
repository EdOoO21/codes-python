from fnmatch import *

for i in range(320000540511, (10 ** 13) + 1)[::519]:
    if (fnmatch(str(i), '32*54?123')) and (str(i).count('0') == 0):
        a = 0
        b = 0
        l = str(i)
        for n in range(12):
            if n <= 5:
                a += int(l[n])
            elif n > 5:
                b += int(l[n])
        if a == b:
            print(i, i // 519)
    if i > 329999549123:
        print('=====================')
        break
