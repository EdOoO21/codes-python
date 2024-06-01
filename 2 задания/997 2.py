print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (z or (not(w <= x)) or ((not (z)) <= (not(y)))) == 0:
                    print(x,y,w,z)