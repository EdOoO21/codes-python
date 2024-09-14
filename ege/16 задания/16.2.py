def F(n):
    if n > 3:
        return F(n - 1) * F(n - 2)
    else:
        return n
print(F(6))

