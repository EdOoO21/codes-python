print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((z <= w) or (y == w)) and ((x or z) == y)) == 1:
                    print(x,y,w,z)

z,y,x,w = 0,0,0,1

print((((z <= w) or (y == w)) and ((x or z) == y)) == 1)