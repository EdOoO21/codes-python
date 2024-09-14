from fnmatch import fnmatch
for i in range(220002,(10**7) + 1,111):
    if fnmatch(str(i),'22?0*5?'):
        print(i,i // 111)