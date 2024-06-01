a = tuple(set((map(int, str(input()).split()))))
b = tuple(set((map(int, str(input()).split()))))
d = {}
counter = 0
for i in a:
    if d.get(i) is None:
        d[i] = 1
    else:
        d[i] += 1
for i in b:
    if d.get(i) is not None:
        counter += 1

print(counter)




