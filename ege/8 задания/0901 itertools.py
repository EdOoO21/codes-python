from itertools import *
counter = 0
for i in combinations('abcdefghijklmnopqrstuvwxyz',10):
    if (i.count('a') + i.count('e')+i.count('i')+i.count('o')+i.count('u')) >= 2:
        print(i)
        counter += 1

print(counter)