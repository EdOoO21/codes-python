a = [int(x) for x in open('17_8475.txt')]

minv = 9999999
for x in a:
    if (abs(x) % 10 == 8) and len(str(abs(x))) == 3:
        minv = min(minv, x)
print(minv)
minv = minv ** 2
s = []
for i in range(len(a) - 2):
    if ((a[i] ** 2 > minv) + (a[i + 1] ** 2 > minv) + (a[i + 2] ** 2 > minv)) == 2:
        if len(str(abs(a[i]))) == 3 or len(str(abs(a[i + 1]))) == 3 or len(str(abs(a[i + 2]))) == 3:
            s.append(a[i] + a[i + 1] + a[i + 2])
            print(a[i], a[i + 1], a[i + 2])

print(len(s), max(s))
