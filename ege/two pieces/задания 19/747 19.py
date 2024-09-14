def f(x,y,p):
    if (x < 10 or y < 10) and p == 3:
        return 1
    if ((x < 10 or y < 10) and p != 3) or (x >= 10 and y >= 10 and p == 3):
        return 0
    if p % 2 == 0:
        return any([f(x-1,y,p+1),f(x-3,y,p+1),f(x,y-1,p+1),f(x,y-3,p+1)])
    else:
        return all([f(x-1,y,p+1),f(x-3,y,p+1),f(x,y-1,p+1),f(x,y-3,p+1)])

for s in range(6,100):
    if f(s,s,1):
        print(s)