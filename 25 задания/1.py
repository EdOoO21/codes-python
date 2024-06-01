s = '11' + '223'
if int(s) % 149 == 0:
    print(s, int(s) // 149)

for k in range(10):
    for n3 in range(10):
        s = '11' + str(n3) + '223'
        if int(s) % 149 == 0:
            print(s, int(s) // 149)


for n2 in range(10):
    for n3 in range(10):
        s = '11' + str(n2) + str(n3) + '223'
        if int(s) % 149 == 0:
            print(s, int(s) // 149)


for n1 in range(10):
    for n2 in range(10):
        for n3 in range(10):
            s = '11' + str(n1) + str(n2) + str(n3) + '223'
            if int(s) % 149 == 0:
                print(s,';', int(s) // 149)





