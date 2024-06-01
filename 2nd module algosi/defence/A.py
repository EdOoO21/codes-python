r = int(input())
i = int(input())
c = int(input())

if i == 0 and r != 0:
    print(3)
elif i == 0 and r == 0:
    print(c)
elif i == 1:
    print(c)
elif i == 4 and r != 0:
    print(3)
elif i == 4 and r == 0:
    print(4)
elif i == 6:
    print(0)
elif i == 7:
    print(1)
else:
    print(i)


