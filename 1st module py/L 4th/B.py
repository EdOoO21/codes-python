import sys
def factorials(n):
    s=1
    for i in range(n):
        yield s
        s *= i + 2


exec(sys.stdin.read())
print(list(factorials(7)))