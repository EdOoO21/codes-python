k = 0
for i in range(10000, 100000):
    n = i
    s = []
    ZeroCounter = 0
    ZeroCounterFail = 0
    ZeroFounder = 0
    while n > 0:
        s.append(n % 9)

        if n % 9 == 0 and ZeroCounter != 0:
            ZeroCounterFail = 1
            break
        elif ZeroCounter == 0 and n % 9 == 0:
            ZeroFounder += 1

        n //= 9
    if ZeroFounder == 1 and ZeroCounterFail == 0 and s[s.index(0) - 1] % 2 == 0\
            and s[s.index(0) + 1] % 2 == 0:
        k += 1
        print(s)

print(k)