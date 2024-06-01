f = open('26-1.txt')
n, k, m = map(int, f.readline().split())
blocks = []
sp = [0] * n
for i in range(n):
    sp[i] = list(map(int,f.readline().split()))

sp = sorted(sp, key=lambda i: (i[1]))
sp = sorted(sp, reverse=True, key=lambda i: (i[0]))
a = []
while len(sp) > 0 or len(a) > 0:
    if len(a) == 0:
        a.append(sp[0])
        sp.pop(0)
    else:
        for i in range(len(sp)):
            if sp[i] != 0 and a[-1][0] - sp[i][0] >= k and a[-1][1] != sp[i][1]:
                a.append(sp[i])
                sp[i] = 0

            if len(a) == m:
                break
        blocks.append(a)
        a = []
    while sp.count(0) > 0:
        sp.remove(0)
print(len(blocks),end=' ')
l = 0
for i in blocks:
    if len(i) == 15:
        l += 1
print(l)

# for i in range(len(sp)):
#     if len(a) == 0 and sp[i] != 0:
#         a.append(sp[i])
#         sp[i] = 0
#     elif sp[i] == 0:
#         continue
#     else:
#         input.txt = 0
#         while len(a) < m:
#             if type(sp[input.txt]) == list:
#                 if len(sp) > input.txt and ((abs(a[-1][0] - sp[input.txt][0])) >= k) and (a[-1][1] != sp[input.txt][1]):
#                     a.append(sp[input.txt])
#                     sp[input.txt] = 0
#
#             input.txt += 1
#             if input.txt == len(sp):
#                 break
#
#     if len(a) == m:
#         blocks.append(a)
#         a = []
#
#     if (len(sp) - 1 == i or sp.count(0) == len(sp)) and len(a) != 0:
#         blocks.append(a)
#
#
# maxv = 0
# for i in blocks:
#     maxv = max(m, len(i))
#     if len(i) != 15:
#         print('='*100)
# counter = 0
# for i in blocks:
#     if len(i) == maxv:
#         counter += 1
#
# print(len(blocks),counter)
# while len(a) < m:
#     if len(sp) == 0:
#         break
#     if sp[i] != 0 and a[-1][0] - sp[i][0] >= k and a[-1][1] != sp[i][1]:
#         a.append(sp[i])
#         sp[i] = 0
#     if i == len(sp) - 1:
#         break
#     i += 1
