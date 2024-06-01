def f(n):
    n = int(input())
    if n != 0:
        return f(n)
    else:
        print(n)

f(1)