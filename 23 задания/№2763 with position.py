def f(n,p):
    if p == 7 and n == 25:
        return True
    elif (p == 7 and n!=25 )or (p!=7 and n==25):
        return False

    return f(n+1,p+1) + f(n+3,p+1) + f(n*2,p+1)

print(f(2,0))