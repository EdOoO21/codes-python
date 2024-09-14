f = open('26.txt')
n = int(f.readline())
a = [list(map(int, s.split())) for s in f]
a.sort()
lg = [0] * 80
gr = [0] * 20
collg = 0
colob = 0

for i in a:
    if i[2] == 0:
        for n in range(len(lg)):
            if i[0] >= lg[n]:
                lg[n] = i[0] + i[1]
                collg += 1
                break
        else:
            for m in range(len(gr)):
                if i[0] >= gr[m]:
                    gr[m] = i[0] + i[1]
                    collg += 1
                    break
            else:
                colob += 1
    else:
        for m in range(len(gr)):
            if i[0] >= gr[m]:
                gr[m] = i[0] + i[1]
                break
        else:
            colob += 1

print(collg, colob)
