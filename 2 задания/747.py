print('='*100,'\n','zadanie 2 :')
print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((x or y or z) <= (x and (y or w))) == 0:
                    print(x,y,w,z)
print('='*100,'\n','zadanie 6 :')


