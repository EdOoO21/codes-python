s = []
def F(n):
    print('*',end='')
    s.append('*')
    if n >= 1:
        print('*',end='')
        s.append('*')
        F(n - 1)
        F(n // 3)
        print('*',end='')
        s.append('*')



F(280)
print(len(s))