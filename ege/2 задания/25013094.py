print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x == (y <= z))) == 0:
                print(x, y, z)

