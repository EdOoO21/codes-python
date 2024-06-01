counter = 0
s = [1, 3, 5, 7, 9]
for i in range(1000000, 10000000):
    n = i
    Win = 1
    FlagOn6 = 0
    no = 0
    while n > 0:
        if FlagOn6 == 1 or no > 2:
            Win = 0
            break
        if n % 9 == 6:
            FlagOn6 = 1
        if n % 9 in s:
            no += 1

        n //= 9

    if no != 2:
        Win = 0

    if Win == 1:
        counter += 1
    print(i)
print(counter)
