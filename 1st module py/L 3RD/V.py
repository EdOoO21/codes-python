def C(k, n):
    if k - 1 == n or k == 0:
        return n
    return C(k - 1, n - 1) + C(k, n - 1)


a, b = int(input()), int(input())
print(C(a, b))
