count = 0
for i in range(-1000,10000):
    s = i
    s //=15
    n = 14
    while s < 285:
        if (s+n)%9 == 0:
            s+=11
        n+=13
    if n == 118:
        print(i)
        count+=1
print(count)
    
