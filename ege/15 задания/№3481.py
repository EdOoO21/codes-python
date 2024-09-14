def f(x,y,A):
    return (((y - 20 < A) and (10 - x < A)) or (x*(y+2) > 48)) == 1

for A in range(-100,10001):
    ok = True
    for x in range(1,1000):
        for y in range(1,1000):
            if not(f(x,y,A)):
                ok = False
    if ok:
        print(A)