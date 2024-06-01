f = open('24 (17).txt').readline()

col = 1
m = 0
for i in range(len(f) - 1):
    if f[i] != f[i + 1]:
        col += 1
        m = max(m,col)
    else:
        col = 1
print(m)