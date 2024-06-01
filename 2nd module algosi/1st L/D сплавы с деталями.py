n, k, m = map(int, str(input()).split())
extra = n
zagotovki = 0
detali = 0
if not(n >= k and k >= m):
    print(0)
else:
    while extra >= k:
        extra = n % k
        zagotovki = n // k
        detali += zagotovki * (k // m)
        extra += zagotovki * (k % m)
        n = extra

    print(detali)


# (n < k) or (k < m) or (n < m)