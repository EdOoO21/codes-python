def f(x,y):
    if x > y or x == 15:
        return False
    if x==y:
        return True
    if x<y:
        return (f(x+1,y) + f(x+3,y))

print(f(2,10)*f(10,20))