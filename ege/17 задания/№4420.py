a = [0] * 4500

for i in range(4500):
    a[i] = int(input())
ans = []
k = 0
for i in range(1,4499):
    if a[i] % 2 == 1 and a[i] > 0 and 100 <= a[i] <= 999 and (a[i - 1] % 2 == 0
        or a[i-1] < 0 or a[i-1] < 100
        or a[i-1] > 999) and (a[i+1] % 2 == 0
        or a[i+1] < 0 or a[i+1] <100
        or a[i+1] > 999):

        k+=1

        ans.append(a[i-1] + a[i] + a[i+1])

print(k,max(ans))