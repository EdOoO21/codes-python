def d(x,L):
    return x % L == 0
def fun(x, A):
    return (not(d(x,18))) <=((not(d(x, 21))) <= (not(d(x, A))))
for A in range(1,10000):
    OK = True
    for x in range(1,1000):
        if not(fun(x, A)):
            OK = False
            break
    if OK:
        print(A)