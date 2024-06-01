def h(n, s=1, f=3):
    if n == 1:
        print(1, s, f)
        return
    h(n - 1, s, 6 - s - f)
    print(n, s, f)
    h(n - 1, 6 - s - f, f)
h(5)
