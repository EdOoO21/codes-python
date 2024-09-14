for i in range(1000):
    string = bin(i)[2:]
    for n in range(3):

        a = list(str(int(string, 2)))
        a = [int(x) for x in a]
        s = sum(a)
        if s % 2 == 1:
            string += '1'
        else:
            string += '0'

    print(a)


