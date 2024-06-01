f = open('26-bag.txt')
k = int(f.readline())
n = int(f.readline())
sp = [0]*n
for i in range(n):
    sp[i] = list(map(int,f.readline().split()))

sp = sorted(sp,key=lambda i:(i[0],i[1],i[2]))
print(sp)
yach = [0] * k

ans = []
for i in sp:
    if i[2] < 50:
        for j in range(k):
            if yach[j] < i[0]:
                yach[j] = i[1]
                ans.append(j + 1)
                break
    else:
        for j in range(k):
            if yach[j] + 3 <= i[0]:
                yach[j] = i[1]
                ans.append(j + 1)
                break

print(len(ans),ans[-1])

