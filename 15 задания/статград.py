P = list(range(69, 92))
Q = list(range(77, 115))
A1 = []
for A in list(range(1, 10000)):
    ok = True
    for x in range(1, 1000):
        if ((x in Q) <= (((x in P) == (x in Q)) or (not (x in P) <= (x in A)))) == 0:
            ok = False
            break
    if ok:
        print(A)