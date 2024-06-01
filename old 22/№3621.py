for i in range(10000):
    x = i
    S = 5
    while x > 0:
        if x % 8 > 4:
            S = S + (x % 8)
        else:
            S = S * (x % 8)
        x = x // 8
    if S % 100 == 0 and S !=0 :
        print(i,S)
        break