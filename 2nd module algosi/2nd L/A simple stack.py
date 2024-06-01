a = []
n = str(input())
while n != 'exit':
    if n.split()[0] == 'push':
        a.append(n.split()[-1])
        print('ok')
    elif n == 'pop':
        print(a[-1])
        a.pop(-1)
    elif n == 'back':
        print(a[-1])
    elif n == 'size':
        print(len(a))
    elif n == 'clear':
        a = []
        print('ok')
    n = str(input())
print('bye')