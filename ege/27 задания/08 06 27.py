def razl(n1):
    n = n1
    i = 2
    p = 1
    c = 0
    while p != n1:
        if n % i == 0:
            p *= i
            n /= i
            c += 1
        else:
            i += 1
    return 
f = open('27A1.txt')
n = int(f.readline())
a = [[int(x), razl(int(x))] for x in f]
print(a)
counter = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[i][1] + a[j][1]) >= 10) and ((a[i][0] + a[j][0]) % 1111 == 0) and i != j:
            counter += 1

print(counter)
print(razl(1000))
for i in range(1, 73083):
    if 73083 % i == 0:
        print(i)
