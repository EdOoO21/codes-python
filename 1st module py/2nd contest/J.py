a = list(map(int, str(input()).split()))
while abs(min(a)) % 2 == 0:
    a.remove(min(a))
print(min(a))