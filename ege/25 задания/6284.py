from fnmatch import *

for i in range(2053323, (10 ** 10) + 1, 1017):
    if fnmatch(str(i), '2?5432*1') and '9' in str(i):
        print(i, i // 1017)
