def f(n):
    if n < 3:
        return 2**n
    elif n == 3:
        return 7
    else:
        return 2*f(n-1) - f(n-4)

n = int(input())
print(n)

