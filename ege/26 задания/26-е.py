f=open('26-1.txt')
a=[list(map(int,s.split())) for s in f]
a.sort(key=lambda i:(-i[0],i[1]))
c=[[[10000, 0]]]
for i in range(1,len(a)):
    for j in range(len(c)):
        if len(c[j])==15: continue
        else:
            if (c[j][-1][0]-a[i][0])>=20 and c[j][-1][1]!=a[i][1]:
                c[j].append(a[i])
                break
    else:
        c.append([a[i]])
m=0
for k in c:
    if len(k)==15:
        m+=1
    print(k)

print(len(c),m)
print(c[671],c[672])