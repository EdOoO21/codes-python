from fnmatch import *
for i in range(38400,(10**8) + 1,768):
    if fnmatch(str(i),'38*56?') and (fnmatch(str(i),'38*2*56?') == 0) and i % 10 != 0:
        print(i,i // 768)