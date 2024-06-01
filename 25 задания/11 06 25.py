from fnmatch import *
for i in range(287127,(10**9) + 1,183):
    if fnmatch(str(i),'??287*139'):
        print(i,i // 183)