n, a = int(input()), tuple(map(int, str(input()).split()))
print(a[len(a) // 2])
# n = int(input())
# a = tuple(map(int, str(input()).split()))
minvalue = sum(a)
minindex = 0
for i in range(a[0], a[-1] + 1):
    b = [abs(x - i) for x in a]
    if (minvalue >= sum(b)) or (i == a[0]):
        minvalue = sum(b)
        minindex = i

print(minindex)
