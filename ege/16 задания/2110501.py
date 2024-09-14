def f(n):
    if n == 0:
        return 0
    if n % 3 == 0 and n > 0:
        return f(n/3)
    if n % 3 != 0:
        return f(n-1) + 1
s = []

for i in range(120,160)[::1]:
    s.append(f(i))
    print(i,' == ',f(i))
    if f(i) == 11:
        print('============================')
        break
print(max(s))

#1455000000,1500000001