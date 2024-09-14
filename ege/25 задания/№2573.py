for i in range(190061, 190073):
    s = []
    for n in range(1, i + 1):
        if i % n == 0 and n % 2 == 1:
            s.append(n)
            if len(s) > 4:
                break
    if len(s) == 4:
        print(i,s[len(s)-1],s[len(s)-2])
