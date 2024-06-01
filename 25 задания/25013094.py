c = 0
for i in range(800001, 1000000000)[::+2]:
    summa = 0
    proz = 1
    counter = 0

    for n in range(1, (i // 2) + 3):

        if i % n == 0:

            counter += 1
            summa += n
            proz *= n



    if proz % 2 == 1 and summa % 2 == 1 and counter > 10:
        print(i, counter)
        c += 1
        if c == 6:
            break
