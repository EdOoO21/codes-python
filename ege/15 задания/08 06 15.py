for a in range(0, 1000):
    if all(((x >= 11) or (3 * x < y) or (x * y < a)) == True for x in range(250) for y in range(250)):
        print(a)
        break
