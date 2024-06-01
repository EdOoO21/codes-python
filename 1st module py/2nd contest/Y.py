n, m = map(int, str(input()).split())
a = []
ans = [0]*n
for i in range(m):
    x, y = str(input()).split()
    a += [[x, y]]
d = {}
a = a[::-1]
for i in a:
    if d.get(i[1]) is None:
        ans[int(i[0])-1] += 1
        d[i[1]] = 0
    else:
        d[i[1]] = 0
print(*ans,sep=' ')
# a, b = '', ''
# ans = [0] * n
# for i in range(m):
#     x, y = str(input()).split()
#     a += ' ' + x + ' '
#     b += ' ' + y + ' '
# a = tuple(a.split())
# b = tuple(b.split())
# for i in range(m):
#     f = set(b[i + 1:])
#     if b[i] not in f:
#         ans[int(a[i]) - 1] += 1
#
# print(*ans, sep=' ')

# n, m = map(int, str(input()).split())
# a,b = [],[]
# ans = [0] *n
# for i in range(m):
#     x,y = str(input()).split()
#     a += [int(x)]
#     b += [y]
#
# for i in range(m):
#     if b[i] not in b[i+1:]:
#         ans[a[i] - 1] += 1
# print(*ans,sep=' ')
