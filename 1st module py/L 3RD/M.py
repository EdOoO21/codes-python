a = int(input())

def f(a):
    for i in range(2,int(a**0.5) + 2):
        if a % i == 0:
            return i
    return a

print(f(a))