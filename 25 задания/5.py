from fnmatch import *

for i in range(1275,10**6+1,51):
    if fnmatch(str(i),'12*45*')==1 and i % 51 == 0:
        print(i,i//51)

