for i in range(194441, 196501):
    s = []
    for n in range(2,(i//2)+1):
        if i % n == 0:
            s.append(n)
    if len(s) % 2 == 1:
        for k in s:
            if k**2 == i:
                print(i,k)
                break
