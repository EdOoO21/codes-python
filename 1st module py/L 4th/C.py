import sys
def triangular_numbers(n):

    for i in range(1,n+1):
        yield (i * (i + 1))//2


exec(sys.stdin.read())

print(list(triangular_numbers(7)))
