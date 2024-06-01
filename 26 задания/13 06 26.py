f = open('26 (11).txt')
k1 = int(f.readline())
n = int(f.readline())
sp = [list(map(int, x.split())) for x in f]
sp = sorted(sp, key=lambda i: i[0])
ochered = []
ops = [0] * k1
ans = []
a = []
for i in range(1, 86400):
    while len(sp) != 0 and i == sp[0][0]:
        a.append(sp[0])
        sp.pop(0)
    for b in range(len(ochered)):
        if ochered[b][1] <= i:
            ochered[b] = 0
    while ochered.count(0) > 0:
        ochered.remove(0)
    if len(ochered) > 0:
        for x in range(k1):
            if i >= ops[x]:
                ops[x] = ochered[0][1]
                ans.append(ochered[0] + [x + 1])
                ochered.pop(0)
            if len(ochered) == 0:
                break
    for c in a:
        fl = 0
        for x in range(k1):
            if c[0] >= ops[x]:
                ops[x] = c[1]
                ans.append(c + [x + 1])
                fl = 1
                break
        if fl == 0:
            ochered.append(c)
    a = []
print(len(ans),ans[-1][-1],ans)
# for i in sp:
#     if len(ochered) != 0:
#         l = sorted(list(set(ops)),reverse=True)
#         if l[-1] == 0:
#             l.pop(-1)
#         if len(l) > 0:
#             for x in range(k1):
#                 if ops[x] <= i[0] and l[-1] == ops[x]:
#                     ops[x] = ochered[0][1]
#                     ans.append(ochered[0] + [x + 1])
#                     ochered.pop(0)
#                 if len(ochered) == ochered.count(0):
#                     break
#     fl = 0
#     for m in range(k1):
#         if ops[m] <= i[0]:
#             ops[m] = i[1]
#             ans.append(i + [m + 1])
#             fl = 1
#             break
#     if fl == 0:
#         ochered.append(i)
#
# print(len(ans), ans[-1][-1],ans)
# for i in sp:
#     for h in range(len(ochered)):
#         l = sorted(list(set(ops)), reverse=True)
#         if l[-1] == 0:
#             l.pop(-1)
#         for x in range(k1):
#             if ops[x] <= i[0] and ops[x] == l[-1]:
#                 ops[x] = ochered[h][1]
#                 ans.append(ochered[h] + [x + 1])
#                 ochered[h] = 0
#                 l[-1] = 0
#                 break
#     while ochered.count(0) > 0:
#         ochered.pop(0)
#
#     if len(ochered) != 0:
#         for k in range(len(ochered)):
#             if ochered[k][1] <= i[0]:  # убрать переждавших
#                 ochered[k] = 0
#         while ochered.count(0) > 0:
#             ochered.pop(0)
#     fl = 0
#     l = sorted(list(set(ops)), reverse=True)
#     if l[-1] == 0:
#         l.pop(-1)
#     for m in range(k1):
#         if ops[m] <= i[0] and ops[m] == l[-1]:
#             ops[m] = i[1]
#             ans.append(i + [m + 1])
#             fl = 1
#             break
#     if fl == 0:
#         ochered.append(i)
#
# print(len(ans), ans[-1][-1])
# ===================================================================================
