def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) + 2*q(n-1)
def q(n):
    if n == 1:
        return 1
    if n > 1:
        return q(n-1) - 2*f(n-1)

print(f(5)+q(5))