n = int(input())
a = [0]*n
for i in range(n):
    a[i] = str(input())
l = str(input())
for i in a:
    if l in i:
        k = i.split()
        if k[0]!=l:
            print(k[0])
        else:
            print(k[1])