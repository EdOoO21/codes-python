import sys
def square_fibonacci(n):
    a = []
    for i in range(n):
        if i <= 1:
            a.append(1)
            yield 1
        else:
            a.append(a[i-2] + a[i-1])
            yield (a[i-2] + a[i-1])**2

exec(sys.stdin.read())

print(list(square_fibonacci(7)))