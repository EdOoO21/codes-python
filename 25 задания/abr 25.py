from fnmatch import *
for i in range(120228,(10**8) + 1,129):
    if fnmatch(str(i),'12?3*46'):
        print(i,i//129)