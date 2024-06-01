f = open('26 (8).txt')
n, k, m = int(f.readline()), int(f.readline()), int(f.readline())
cams = [[] for _ in range(k)]

sp = [int(x) for x in f]
sp = sorted(sp, reverse=True)
index = 0
ans = []
for i in range(len(cams)):
    n = 0
    sp.sort(reverse=True)
    while (sum(cams[i]) + sp[n]) <= m:
        cams[i].append(sp[n])
        sp[n] = 0
        ans.append(i)
        n += 1
        if not (n <= len(sp) - 1):
            break
    # =====================================================

    while sp.count(0) > 0:
        sp.remove(0)
    if len(sp) == 0:
        break
    # =====================================================
    sp.sort()
    n1 = 0
    while (sum(cams[i]) + sp[n1]) <= m:
        cams[i].append(sp[n1])
        sp[n1] = 0
        ans.append(i)
        n1 += 1
        if not (n1 <= len(sp) - 1):
            break

    # =====================================================
    while sp.count(0) > 0:
        sp.remove(0)
    if len(sp) == 0:
        break

print(ans[-1] + 1, m - sum(cams[ans[-1]]))



# f = open('26 (8).txt')
# n = int(f.readline())
# k = int(f.readline())
# m = int(f.readline())
# a = [int(input.txt) for input.txt in f]
# c = []
# while len(a) != 0:
#     fl = True
#     a.sort(reverse=True)
#     b = [a.pop(0)]
#
#     input.txt = b[0]
#     i = 0
#     while sum(b) < m and i < len(a):
#         if input.txt + a[i] <= m:
#             input.txt += a[i]
#             b.append(a.pop(i))
#         else:
#             a.sort()
#             i = 0
#             while input.txt < m:
#                 if input.txt + a[i] <= m:
#                     input.txt += a[i]
#                     b.append(a.pop(i))
#                 else:
#                     fl = False
#                     break
#             if fl == False:
#                 break
#
#     c.append(b)
# print(c)
# print(c[-1], len(c), m - sum(c[-1]))
