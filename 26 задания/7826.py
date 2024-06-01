f = open('26_7826.txt')
k,n = map(int,f.readline().split())
sp = f.readlines()
for i in range(n):
    sp[i] = list(map(int,sp[i].split()))
sp = sorted(sp,key=lambda i:i[0])
attr = [0]*k

a = []
counter = 0
posl = []
for i in range(len(sp)):
    a.append(sp[i])
    if len(sp) > i + 1 and sp[i][0] == sp[i + 1][0]:
        continue
    if len(a) == 1:
        for h in range(k):
            if attr[h] < a[0][0]:

                posl += [h + 1]
                attr[h] = a[0][1]
                a = []
                counter += 1
                break
    if len(a) > 1:
        a = sorted(a,key=lambda j:j[1],reverse=True)
        for h in range(k):
            if attr[h] < a[0][0]:

                posl += [h + 1]
                attr[h] = a[0][1]
                counter += len(a)
                a = []
                break
    a = []

print(counter,posl[-1])


