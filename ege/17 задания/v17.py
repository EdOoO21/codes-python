a = [int(x) for x in open('17.txt')]

ans = []
maxv =0
ans1 = []
for i in range(len(a) - 1):
    if ((abs(a[i]) % 10 == 1) + (abs(a[i + 1]) % 10 == 1)) == 1:
        maxv = max(maxv,(a[i] + a[i+1])/2)
        ans1.append([a[i],a[i+1]])

counter = 0
for i in ans1:
    if i[0] < maxv and i[1] < maxv:
        ans.append([i[0],i[1]])


ans = sorted(ans,key=lambda i:i[0])
print(len(ans),ans)





