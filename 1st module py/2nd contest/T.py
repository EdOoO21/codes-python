s, n, f = [], ' ', open('input.txt')
while n != '':
    n = f.readline()
    s += n.split()
d = {}
for i in s:
    if d.get(i) is None:
        d[i] = 1
    else:
        d[i] += 1

d = dict(sorted(d.items(), key=lambda i: (-i[1], i[0])))
print(list(d.keys())[0], d)
