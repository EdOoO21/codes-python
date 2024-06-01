from fnmatch import *

for i in range(810066,(10**8)  + 1,237):
    if fnmatch(str(i),'81?2*80') and fnmatch(str(i),'*9*') == 0:
        print(i,i // 237)