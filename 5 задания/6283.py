s = 0
for n in range(11, 100000):
    i = bin(n)[2:]

    if n % 10 == 0:
        n1 = i + i[-4:]

    else:
        n1 = i + bin(((int(str(n)[-1]) ** 2) // 2))[2:]

    if int(n1, 2) < 680:
        s += 1


print(s)
