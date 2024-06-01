counter = 0
for a in range(10):
    n = '1' + str(a) + '49341'
    if (int(n) % 2023) == 0:
        print(n)
        counter += 1

for a in range(10):
    for b in range(10):
        n = '1' + str(a) + '493' + str(b) + '41'
        if (int(n) % 2023) == 0:
            print(n)
            counter += 1

for a in range(10):
    for b in range(10):
        for c in range(10):
            n = '1' + str(a) + '493' + str(b) + str(c) + '41'
            if (int(n) % 2023) == 0:
                print(n)
                counter += 1

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                n = '1' + str(a) + '493' + str(b) + str(c) + str(d) + '41'
                if (int(n) % 2023) == 0:
                    print(n)
                    counter += 1

print(counter)
