# поразрядная сортировка
def radix_sort(ans):
    max_digit = max([len(x) for x in ans])
    digits = [[] for _ in range(10)]
    print('Initial array:')
    print(*ans, sep=', ')
    for i in range(max_digit):
        print('**********')
        print(f'Phase {i + 1}')
        for k in ans:
            digits[(int(k) // 10 ** i) % 10].append(k)
        ans = [x for dig in digits for x in dig]
        for i in range(len(digits)):
            if len(digits[i]) == 0:
                print(f'Bucket {i}: empty')
            else:
                print(f'Bucket {i}: ', end='')
                print(*digits[i], sep=', ')

        digits = [[] for _ in range(10)]
    return ans


n = int(input())
a = [str(input()) for _ in range(n)]
a = radix_sort(a)
print('**********')
print('Sorted array:')
print(*a, sep=', ')
