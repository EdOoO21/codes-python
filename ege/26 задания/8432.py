f = open('26_8432 (4).txt')
n = int(f.readline())
park = [[0 for _ in range(70)], [0 for _ in range(30)]]
sp = []
for i in f:
    sp.append(list(map(int, i.split())))
sp = sorted(sp, key=lambda i: i[0])
counter = 0
cc = 0
for i in sp:
    fl1 = 0
    fl = 0
    if i[2] == 0:
        for k in range(30):
            if park[1][k] <= i[0]:
                park[1][k] = i[0] + i[1]
                cc += 1
                fl1 = 1
                break
    else:
        for k in range(70):
            if park[0][k] <= i[0]:
                park[0][k] = i[0] + i[1]
                fl = 1
                break
        if fl == 0:
            for k1 in range(30):
                if park[1][k1] <= i[0]:
                    park[1][k1] = i[0] + i[1]
                    fl = 1
                    break
    if fl == 0 and fl1 == 0:
        counter += 1
print(cc,counter)