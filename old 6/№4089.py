for i in range(-100,1000):
    s = i
    n = 2
    while s<64:
        s+=8
        n*=2
    if n == 256 :
        print(i)