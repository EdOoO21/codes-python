f = open('9 (41).txt')
sp = [0]*3200

for i in range(3200):
    sp[i] = list(map(int,f.readline().split()))
    if sp[i].count(sp[i][0]) + sp[i].count(sp[i][1]) + sp[i].count(sp[i][2]) + sp[i].count(sp[i][3]) + sp[i].count(sp[i][4]) == 9:
        srp = []
        srnep = []
        for k in sp[i]:
            if sp[i].count(k) == 2:
                srp.append(k)
            else:
                srnep.append(k)

        if sum(srp) / 4 > sum(srnep):
            print(sp[i],sum(srp) / 4 , sum(srnep))