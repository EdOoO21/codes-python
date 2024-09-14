f = 0
for i in range(600000,1000000):
    if f == 5:
        break
    else:
        s = []
        c = 0
        for n in range(2,(i//2)+1):
            if i % n == 0:
                if n % 10 == 7 and n!=7:
                    s.append(n)
                    c +=1
                    break
        if c != 0:
            print(i,min(s))
            f+=1
                
