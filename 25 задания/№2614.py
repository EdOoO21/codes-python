for i in range(1523467, 4157812+1):
    k = 0
    s = []
    for n in range(2,(i//2)+1):
        if i % n == 0 :
            k += 1
            s.append(n)
        if k > 3:
            s = []
            k = 0
            break
    if len(s) == 3:
        print(i,max(s))
