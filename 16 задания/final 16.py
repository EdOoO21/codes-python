def f(x):
    if x <= 1:
        return 1
    if x % 4 == 0:
        return f(x//2) + f(x//4) + (x//4)
    if x % 2 == 0 and x % 4 != 0:
        return f(x // 2) + (x // 2)
    else:
        return f(x - 1) + f(x - 4)

print(f(10000))