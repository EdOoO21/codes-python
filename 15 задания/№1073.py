def fun(x, y, A):
    return (5*y + 7*x != 129) or (3*x > A) or (4*y > A)
for A in range(1,10000):
    OK = True
    for x in range(1,1000):
        for y in range(1,1000):
            if not(fun(x, y, A)):
                OK = False
                break
    if OK:
        print(A)