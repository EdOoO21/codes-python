n = int(input())
for k in range(n):
    line = list(map(float, input().split()))
    line.pop(0)
    sorted_line = sorted(line)
    index = 0
    stack = []
    i = 0
    while i < len(line):
        if (len(stack) > 0) and (sorted_line[index] == stack[-1]):
            stack.pop(-1)
            index += 1
        elif sorted_line[index] == line[i]:
            index += 1
            i += 1
        elif sorted_line[index] != line[i]:
            if (len(stack) > 0) and (line[i] > stack[-1]):
                print(0)
                break
            stack.append(line[i])
            i += 1
    else:

        if (len(stack) != 0) and (stack[0] == sorted_line[-1]):
            print(1)
        elif len(stack) == 0:
            print(1)
        else:
            print(0)



# from random import *
# n = int(input())
# for k in range(n):
#     line=[randint(-1000,1000),randint(-1000,1000),randint(-1000,1000),randint(-1000,1000),randint(-1000,1000)]
#     print(line)
#
#     sorted_line = sorted(line)
#     index = 0
#     stack = []
#     i = 0
#     ans = []
#     while i < len(line):
#         if (len(stack) > 0) and (sorted_line[index] == stack[-1]):
#             stack.pop(-1)
#             index += 1
#         elif sorted_line[index] == line[i]:
#             index += 1
#             i += 1
#         elif sorted_line[index] != line[i]:
#             if (len(stack) > 0) and (line[i] > stack[-1]):
#                 ans[0] = 0
#                 break
#             stack.append(line[i])
#             i += 1
#     else:
#
#         if (len(stack) != 0) and (stack[0] == sorted_line[-1]):
#             ans[0] = 1
#         elif len(stack) == 0:
#             ans[0] = 1
#         else:
#             ans[0] = 0

# from random import randint  #
#
# n = int(input())
# for k in range(n):
#     t = [9, 5, 1, 9, 1]
#     print(t)
#     a = []
#     for i in range(len(t)):
#         if i == 0 or t[i] != t[i - 1]:
#             a.append(t[i])
#     b = []
#     stack = []
#     for i in range(len(a) - 1):
#         while len(b) != 0 and len(stack) != 0 and b[-1] <= stack[0] <= a[i]:
#             b.append(stack.pop(0))
#         if a[i] < a[i + 1] or (len(b) != 0 and b[-1] == a[i]):
#             if len(b) == 0 or b[-1] <= a[i]:
#                 b.append(a[i])
#             else:
#                 print(0)
#                 break
#         else:
#             if len(stack) == 0 or stack[0] >= a[i]:
#                 stack = [a[i]] + stack
#             else:
#                 print(0)
#                 break
#     else:
#         print(1 if len(b) == 0 or len(stack) == 0 or b[-1] <= a[-1] <= stack[0] or b[-1] <= stack[0] <= a[-1] else 0)
#     print(b)
    # line = t
    # sorted_line = sorted(line)
    # index = 0
    # stack = []
    # i = 0
    # while i < len(line):
    #     if (len(stack) > 0) and (sorted_line[index] == stack[-1]):
    #         stack.pop(-1)
    #         index += 1
    #     elif sorted_line[index] == line[i]:
    #         index += 1
    #         i += 1
    #     elif sorted_line[index] != line[i]:
    #         if (len(stack) > 0) and (line[i] > stack[-1]):
    #             ans[1] = 0
    #             break
    #         stack.append(line[i])
    #         i += 1
    # else:
    #     if (len(stack) != 0) and (stack[0] == sorted_line[-1]):
    #         ans[1] = 1
    #     elif len(stack) == 0:
    #         ans[1] = 1
    #     else:
    #         ans[1] = 0
    # if ans[0] != ans[1]:
    #     print(t)
    #     print(ans[0],ans[1])
