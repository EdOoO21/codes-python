def xor(a,b):
    if a + b != 1:
        return 0
    return 1
a,b, = int(input()),int(input())

print(xor(a,b))