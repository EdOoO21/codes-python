for x in range(1,1000000):
    s = (27**7) - (3**11) + 36 - x
    s1 = []
    while s > 0 :
        s1.append(s%3)
        s//=3
    if sum(s1) == 22:
        print(x,s1)
        break


