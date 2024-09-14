ft = []
for a in range(4):
    for b in range(4):
        for c in range(4):
            ft.append(int('13' + str(a) + str(b) + '22' + str(c), 4))

sd = []

for a in range(8):
    for b in range(8):
        sd.append(int('1' + str(a) + str(b) + '50', 8))

td = []
for a in range(16):
    td.append(int(str(a) + 'C28', 16))
print(len(td),len(ft),len(sd))

for a in td:
    for b in sd:
        for c in ft:
            if a == b == c:
                print(a)
# for i in range(4):
#     if int('13' + str(i)*2 + '22' + str(i),4) == int('1' + 2*str(i) + '50',8) == int(str(i)+'C28',16):
#         print(i)
