for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (x and (not(y)) and ((not(z)) or w)) == 1:
                    print(x,y,w,z)
