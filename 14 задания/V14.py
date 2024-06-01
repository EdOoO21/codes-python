for p in range(30):
    for y in range(p):
        for x in range(p):
            for z in range(p):
                if (y * (p**2) + 2 * p + y) + (y * (p**2) + 5 * p + 7) == (x * (p**3) + z * (p**2) + z * p + 3):
                    print(x,y,z,p)
