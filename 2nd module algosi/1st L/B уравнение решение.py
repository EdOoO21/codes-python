a, b, c = int(input()), int(input()), int(input())

if c < 0:
    print('NO SOLUTION')
elif (a == 0) and (b != (c ** 2)):
    print('NO SOLUTION')
elif (a == 0) and (b == (c ** 2)):
    print('MANY SOLUTIONS')
elif (((c ** 2) - b) / a) == (((c ** 2) - b) // a):
    print(((c ** 2) - b) // a)
else:
    print('NO SOLUTION')
