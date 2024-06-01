f = [0] * 10010
for n in range(10000, len(f)):
    f[n] = n
for k in range(2, 9999)[::-2]:
    f[k] = f[k+2] - 3
for k in range(1,10000)[::-2]:
    f[k] = f[k+2] + 1

print(f)
print(f[9994] - f[9980])
