from fnmatch import *

for i in range(130004865,(10**9) + 1,999):
    if fnmatch(str(i),'13*57?9') and len(str(i)) == 9:
        print(i,i //999)