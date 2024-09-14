from fnmatch import *
for i in range(2023,(10**9 ) +1,2023):
    h = 0
    for x in str(i):
        h += int(x)
    if h % 7 == 0 and h < 20 and fnmatch(str(i),'20*23'):
        print(i,i / 2023)