def f(n):
    if n < 2:
        return  1
    if n >= 2 and n % 3 == 0:
        return  f(n / 3) + 1
    if n >= 2 and n % 3 != 0:
        return f(n - 2) + 5
ok = True
k = 1
while ok:
    if f(k) == 73:
        print(k)
        ok = False
    else:
        k+=1
'''''
for n in range(1,100):
    if f(n) == 73:
        print(n)
'''