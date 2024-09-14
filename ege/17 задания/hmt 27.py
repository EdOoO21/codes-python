a = [0] * 5001

for i in range(5001):
    a[i] = int(input())
ans = []
k = 0
for n in range(len(a)):
    if n != len(a) - 1 and a[n] % 2 == 0 and a[n+1] % 2 == 1:
        if a[n] % 4 == 0 and a[n+1] % 11 == 0:
            ans.append(a[n]+a[n+1])
            k+=1
    if n != len(a) - 1 and a[n] % 2 == 1 and a[n+1] % 2 == 0:
        if a[n+1] % 4 == 0 and a[n] % 11 == 0:
            ans.append(a[n]+a[n+1])
            k+=1

print(k,max(ans))