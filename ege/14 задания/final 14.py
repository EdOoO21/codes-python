for x in '0123456789ABCD':
    for y in '0123456789ABCDEFGHIJK':
        a = int('2A9' + x + '4', 14)
        b = int(x + '49C', 18)
        c = int('7' + y + '6' + y, 21)
        if (a + b - c) % 219 == 0:
            print((a + b - c) // 219, end=' ')
            print((4 * int(x, 14) + 3 * int(y, 21)) // 4)
