a = [0] * 50
for i in range(50):
    a[i] = int(input())
k = 0
maxValue = 0
for n in range(49):
    if abs(a[n]) % 10 == 5 and abs(a[n + 1]) % 10 == 5:
        k += 1
        maxValue = max(maxValue,(a[n] + a[n+1]))

print(k,maxValue)
