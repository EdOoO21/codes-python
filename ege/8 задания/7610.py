l = 'аклмня'
counter = 0
f = 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for e in l:
                    w = a+b+c+d+e
                    counter +=1
                    if a == 'к' and b == 'м':
                        print(counter,w)
                        f = 1
                        break
                    print(counter)

                if f == 1:
                    break
            if f == 1:
                break
        if f == 1:
            break
    if f == 1:
        break
