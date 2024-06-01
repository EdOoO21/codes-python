global ans
ans = ''

import sys
sys.setrecursionlimit(1000000)
def f(n, k):
    global ans
    if n == 1:
        if (len(ans) > len(k)) or (not ans):
            ans = k
        return 0
    elif n < 1:
        return 0
    if n % 2 == 0 and n % 3 != 0:
        return f(n - 1, k=k + f'{n - 1}'),f(n // 2, k=k + f'{n // 2}')
    elif n % 3 == 0 and n % 2 != 0:
        return f(n - 1, k=k + f'{n - 1}'), f(n // 3, k=k + f'{n // 3}')
    elif n % 3 == 0 and n % 2 == 0:
        return f(n - 1, k=k + f'{n - 1}'), f(n // 3, k=k + f'{n // 3}'),f(n // 2, k=k + f'{n // 2}')
    else:
        return f(n - 1, k=k + f'{n - 1}')





n = int(input())
if n == 1:
    print(0)
    print(1)

else:
    f(n, k='')
    print(len(ans))
    for i in ans[::-1]:
        print(i,end=' ')
    print(n)