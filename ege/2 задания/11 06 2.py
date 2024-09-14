print('a b c t')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for t in range(2):
                if (((not (a)) or (not (b))) and (c <= (not (a))) and ((t and (not (a))) or (c and (not (b))))) == 1:
                    if a + b + c + t == 1:
                        print(a, b, c, t)
