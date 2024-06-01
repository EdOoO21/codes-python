a = [0] * 20
for i in range(20):
    a[i] = i * 34

for i in range(1,len(a)):
    b = a[i:]
    c = a[:i]
    print(b,c)