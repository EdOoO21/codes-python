count = 0
for i in range(-1000,10001):
    s = i
    s//=9
    n = 12
    while s < 220:
        if (s+n) % 7 == 0:
            s+=7
        n+=17
    if n == 131:
        print(i)
        count+=1
print(count)
