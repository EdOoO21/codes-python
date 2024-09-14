from fnmatch import *

for i in range(1100365, (10 ** 8) + 1, 211):
    if fnmatch(str(i),'11??4*56') == 1 :
        print(i, i // 211)
