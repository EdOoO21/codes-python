for i in range(-10000,10000):
    s = i
    n = 80
    while s+n<160:
        s+=15
        n-=10
    if s <= 100:
        print(i)