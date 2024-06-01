a = list(map(int, str(input()).split()))
s = a[-1]
a.pop(-1)
a = [s] + a
print(*a)