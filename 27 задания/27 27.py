f = open('27B_9078 (1).txt')
n, d, t = list(map(int, f.readline().split()))
a = [int(x) for x in f]
h = ''
for i in range(len(a)):
    if a[i] % d == 0:
        h += '*'
    else:
        h += '+'

print(h.index('*',1 + h.index('*'),len(h)),h.index('*'))
