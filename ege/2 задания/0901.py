print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (w and ((x <= y) == (y <= z))) == 1:
                    print(x, y, w, z)

