def f(x, p):
    if p == 4 and x >= 50:
        return 1
    if (p != 4 and x >= 50) or (p == 4 and x < 50):
        return 0

    if p % 2 == 1:
        return any([f(x + 2, p + 1), f(x * 3, p + 1)])
    else:
        return all([f(x + 2, p + 1), f(x * 3, p + 1)])

counter = 0
for i in range(1,50):
    if f(i,1):
        print(i)
        counter += 1

print('==== ', counter, ' ==== ')  # 3

