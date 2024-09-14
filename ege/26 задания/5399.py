f = open('5399')
n, d = map(int, f.readline().split())

sp = [int(x) for x in f]
sp.sort(reverse=True)

pars = []
i = 0
for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp)):
        if sp[i] + sp[j] <= d and sp[i] != 0 and sp[j] != 0:
            pars.append([sp[i], sp[j]])
            sp[i] = 0
            sp[j] = 0

while sp.count(0) > 0:
    sp.remove(0)

print(len(pars), sum(sp))
