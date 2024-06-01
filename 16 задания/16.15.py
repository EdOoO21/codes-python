def F(n):
    if n > 0:
        print(n)
        F(n - 3)
        F(n // 2)

F(7)