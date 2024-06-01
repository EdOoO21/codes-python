
for i in range(1, 50000000)[::-1]:
    x = i
    a = 0
    b = 0
    while x > 0:
        a += 1
        if x % 2 != 0 :
            b += 1
        x //= 2
    if (a == 24 and b == 4) :
        print(i)
        break

#15728640