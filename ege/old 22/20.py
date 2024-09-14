for i in range(-1000,10000):
    x = i
    a = 1
    while x > 0:
        a *= (x % 11)
        x = (x // 11)
    if a == 120:
        print(i)
        break