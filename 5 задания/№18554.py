for i in range(2,101):
    n = format(i, 'b')
    if n.count('1') > n.count('0'):
        n+='1'
    else:
        n+='0'

    print(i,' = ',n)
