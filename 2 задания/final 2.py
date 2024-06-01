print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((x and y) == (y or w)) <= ((not(z)) or w)) == 0:
                    print(x,y,w,z)