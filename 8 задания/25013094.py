l = 'piton'
k = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                w = a+b+c+d
                if ('ii' not in w) and ('oo' not in w) \
                    and ('io' not in w) and ('oi' not in w) \
                    and ('pp' not in w) and ('tt' not in w)\
                    and ('nn' not in w) and ('pt' not in w)\
                    and ('tp' not in w) and ('pn' not in w)\
                    and ('np' not in w) and ('nt' not in w)\
                    and ('tn' not in w):
                    print(w)
                    k+=1

print(k)
