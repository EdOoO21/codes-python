print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((x and (y or (not (z))) and w) == (x <= (not (y)) and z)) == 1:
                    print(x, y, w, z)
