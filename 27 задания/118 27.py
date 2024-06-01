f = open('27a_8483 (1).txt')
n = int(f.readline())
k = int(f.readline())

a = [int(x) for x in f]
maxv = 0

# for i in range(len(a) - 2 * k):
#     for j in range(i + k, len(a) - k):
#         for p in range(j + k, len(a)):
#             if i != j != p:
#                 maxv = max(maxv, a[i] + a[j] + a[p])
#
# print(maxv)
b = a.copy()
b = sorted(b, reverse=True)
for i in b[:1000]:
    if abs(120 - a.index(i)) >= 30:
        print(i, a.index(i))
        break
l = b.index(4005578)
for i in range(13, 10000):
    if abs(120 - a.index(b[i])) >= 30 and abs(318 - a.index(b[i])) >= 30:
        print(b[i], a.index(b[i]))
        break
summ = 5183293 + 4005578 + 2466414
print(summ)

# ================================================================

f = open('27b_8483 (2).txt')
n = int(f.readline())
k = int(f.readline())
a = [int(x) for x in f]
b = a.copy()
b = sorted(b, reverse=True)

summ1 = 109965797840 + 109932605146 + 109911912389

l1 = a.index(109965797840)
l2 = a.index(109932605146)
l3 = a.index(b[2])
l4 = a.index(b[3])
for i in range(len(b)):
    if abs(l1 - a.index(b[i])) >= k:
        print(b[i], a.index(b[i]), a.index(b[0]))
        break

for i in range(len(b)):
    if abs(l1 - a.index(b[i])) >= k and abs(l2 - a.index(b[i])) >= k:
        print(b[i], a.index(b[i]), l2, l1, b.index(b[i]))
        break

print(summ1,b[0] + b[1] + b[3])


