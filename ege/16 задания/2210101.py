def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1) + n
c = 0
for i in range(0,900):
    if f(i) % 3 != 0:
        c+=1
print(c,900//3)
print(237567892/3)
print((1134567004 - 237567891) / 3)
