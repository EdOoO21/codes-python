a = int(input())


def IsPrime(a):
    if 2 <= a <= 3:
        return 'YES'
    for i in range(2, int(a ** 0.5) + 3):
        if a % i == 0:
            return 'NO'
    return 'YES'


print(IsPrime(a))
