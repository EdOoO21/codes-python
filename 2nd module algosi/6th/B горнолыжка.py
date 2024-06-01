n = int(input())
line1 = [list(map(int, input().split()))[1] for _ in range(n)]
m = int(input())

for l in range(m):
    i = list(map(int,input().split()))
    if i[0] < i[1]:
        arr = (line1[k + 1] - line1[k] if line1[k + 1] - line1[k] > 0 else 0 for k in range(i[0] - 1, i[1] - 1))
    elif i[0] > i[1]:
        arr = (line1[k - 1] - line1[k] if line1[k - 1] - line1[k] > 0 else 0 for k in range(i[0] - 1, i[1] - 1,-1))
    else:
        arr = [0]

    print(sum(arr))

# n = int(input())
# a = [0, 0]
# b = [0, 0]
# x_prev, y_prev = -1, -1
# for i in range(n):
#     x, y = map(int, input().split())
#     if x_prev == -1:
#         x_prev = x
#         y_prev = y
#     elif y > y_prev:
#         a.append(a[-1] + y - y_prev)
#         b.append(b[-1])
#         x_prev = x
#         y_prev = y
#     else:
#         a.append(a[-1])
#         b.append(b[-1] + y_prev - y)
#         x_prev = x
#         y_prev = y
#
# print(a,b)