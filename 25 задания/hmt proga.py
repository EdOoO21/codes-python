simples = []
for i in range(1, (578926//2)+1):
    ok = True
    for n in range(2, (i // 2) + 1):
        if i % n == 0:
            ok = False
            break
    if ok:
        simples.append(i)
print('done')
a = []
for i in simples:
    for n in simples:
        if i * n >= 523456 and i * n <= 578925:
            a.append(i * n)
print('done')
a1 = []
a2 = []
a3 = []
minvalue = 999999999999
for i in a:
    for n in range(2, (i // 2) + 1):
        if i % n == 0 and n in simples:
            a1.append(n)

    for p in range(1, len(a1)):
        if a1[p] - a1[p - 1] < minvalue:
            a2 = []
            a3 = []
            minvalue = a1[p] - a1[p - 1]
            a2.append(a1[p - 1])
            a2.append(a1[p])
            a3.append(i)
print(*a3,*a2)


