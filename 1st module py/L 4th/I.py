a,b = str(input()).split()

try:
    int(a)
except ValueError:
    print('Error: ValueError')
else:
    try:
        int(b)
    except ValueError:
        print('Error: ValueError')
    else:
        try:
            int(a) / int(b)
        except ZeroDivisionError:
            print('Error: ZeroDivisionError')
        else:
            print(int(a)//int(b))