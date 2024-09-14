s = [0] * 1000
maxv = 0
for i in range(1000):
    s[i] = int(input())
    if s[i] > maxv and s[i] % 2 == 1:
        maxv = s[i]

s1 = []
k = 0
for i in range(999):
    if ((s[i] + s[i + 1]) % 2 == 0) and (min(s) + maxv)<(s[i] + s[i + 1]):
        s1.append(s[i] + s[i + 1])
        k+=1
print(k, min(s1))
