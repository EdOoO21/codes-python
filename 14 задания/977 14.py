for x in range(19):
    a = 4 + 7 * 19 + x * (19**2) + 3 * (19 ** 3) + 10 * (19**4)
    b = 6 + 4 * 19 + 8 * (19**2) + 0 * (19 ** 3) + 4 * (19**4) + x * (19 ** 5)
    if (a + b) % 9 == 0:
        print((a + b) / 9,x)