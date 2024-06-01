s = []
def f(n):
    s.append(2*n+1)
    if n > 1:
        s.append(3*n-8)
        f(n-1)
        f(n-4)

f(50)
print(sum(s))