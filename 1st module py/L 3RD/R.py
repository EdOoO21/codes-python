def gcd(a, b):
    if max(a, b) % min(a, b) == 0:
        return min(a, b)
    return gcd(b, abs(a) % abs(b))


a, b = int(input()), int(input())
if a == 0 or b == 0:
    print(0)
else:
    c = (gcd(max(abs(a), abs(b)), min(abs(a), abs(b))))
    if a < 0 and b < 0:
        print(-c)
    else:
        print(c)
