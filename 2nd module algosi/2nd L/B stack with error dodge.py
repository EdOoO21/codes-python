a = []
n = str(input()).split()
while n[0] != 'exit':
    if n[0] == 'push':
        a.append(n[-1])
        print('ok')
    elif (n[0] == 'pop') and (len(a) > 0):
        print(a[-1])
        a.pop(-1)
    elif (n[0] == 'pop') and (len(a) == 0):
        print('error')
    elif (n[0] == 'back') and (len(a) > 0):
        print(a[-1])
    elif (n[0] == 'back') and (len(a) == 0):
        print('error')
    elif n[0] == 'size':
        print(len(a))
    elif n[0] == 'clear':
        a = []
        print('ok')
    n = str(input()).split()
print('bye')