for i in range(5,10000):
    n1 = bin(i)[2:]
    k = n1.count('0')
    n2 = i - k
    n = bin(n2)[2:]
    n += n[len(n) - 3] + n[len(n) - 2] + n[len(n) - 1]
    ans = int(n,2)
    if ans > 224:
        print(i,ans,n)
        break