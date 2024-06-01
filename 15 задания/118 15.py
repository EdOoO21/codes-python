p = [x for x in range(5, 138)]
for a in range(1, 10000):
    s = []
    for x in range(1, 10000):
        s.append((((x % 115 == 0) and (x % 5 != 0)) or ((a % x == 0) <= (a % 5 != 0))) and (a not in p))
    if len(set(s)) == 2:
        print(a)
        break
