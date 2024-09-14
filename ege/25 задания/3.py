for a in range(10):
    s = '3221' + str(a) + '4'
    if int(s) % 2049 == 0:
        print(s, int(s) // 2049)

for a in range(10):
    for n1 in range(10):
        s = '32' + str(n1) + '21' + str(a) + '4'
        if int(s) % 2049 == 0:
            print(s, int(s) // 2049)


for a in range(10):
    for n1 in range(10):
        for n2 in range(10):
            s = '32' + str(n1) + str(n2) + '21' + str(a) + '4'
            if int(s) % 2049 == 0:
                print(s, int(s) // 2049)


for a in range(10):
    for n1 in range(10):
        for n2 in range(10):
            for n3 in range(10):
                s = '32' + str(n1) + str(n2) + str(n3) + '21' + str(a) + '4'
                if int(s) % 2049 == 0:
                    print(s, int(s) // 2049)