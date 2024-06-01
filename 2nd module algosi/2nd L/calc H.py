def f1(t):
    a = []
    for i in range(len(t)):
        if i == 0 or t[i] != t[i - 1]:
            a.append(t[i])
    b = []
    stack = []
    for i in range(len(a) - 1):
        while len(b) != 0 and len(stack) != 0 and b[-1] <= stack[0] <= a[i]:
            b.append(stack.pop(0))
        if a[i] < a[i + 1]:
            if len(b) == 0 or b[-1] <= a[i]:
                b.append(a[i])
            else:
                return 0

        else:
            if len(stack) == 0 or stack[0] >= a[i]:
                stack = [a[i]] + stack
            else:
                return 0
    else:
        if (len(b) == 0) or (len(stack) == 0) or (b[-1] <= a[-1] <= stack[0]) or (b[-1] <= stack[0] <= a[-1]):
            return 1
        else:return 0


def f2(t):
    line = t
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
                return 0

            stack.append(line[i])
            i += 1
    else:
        if (len(stack) != 0) and (stack[0] == sorted_line[-1]):
            return 1
        elif len(stack) == 0:
            return 1
        else:
            return 0


from random import *

n = int(input())
for k in range(n):
    t = [randint(5, 15) for i in range(5)]
    a = f1(t)
    b = f2(t)
    if ((a == 0) and (b == 1)):
        print(t, a, b)
