for k in range(10):
    for n1 in range(10):
        for n2 in range(10):
            for n3 in range(10):
                s = '1' + str(k) + '2139' + str(n1) + str(n2) + str(n3) + '4'
                if int(s) % 2023 == 0:
                    print(s, int(s) // 2023)

for k in range(10):
    for n2 in range(10):
        for n3 in range(10):
            s = '1' + str(k) + '2139' + str(n2) + str(n3) + '4'
            if int(s) % 2023 == 0:
                print(s, int(s) // 2023)

for k in range(10):
    for n3 in range(10):
        s = '1' + str(k) + '2139' + str(n3) + '4'
        if int(s) % 2023 == 0:
            print(s, int(s) // 2023)

for k in range(10):
    s = '1' + str(k) + '2139' + '4'
    if int(s) % 2023 == 0:
        print(s, int(s) // 2023)
