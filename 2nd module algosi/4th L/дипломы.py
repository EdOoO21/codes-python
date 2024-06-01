def bin_poisk(w, h):
    r = w * h * n
    l = 1
    sred = (r + 1) // 2
    ans = 0
    while l <= r:
        if ((sred // w) * (sred // h)) >= n:
            r = sred - 1
            ans = sred
        else:
            l = sred + 1
        sred = (l + r) // 2
    return ans


w1, h1, n = map(int, str(input()).split())

print(bin_poisk(w1, h1))
