for i in range(1,1000):
    n = str(bin(i)[2:])
    n+=n[len(n)-1]
    if n.count('1') % 2 == 0:
        n+='0'
    else:
        n+='1'
    n+='0'
    if int(n,2) > 90:
        print(i,int(n,2),n)


