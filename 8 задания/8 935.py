l = 'епсух'
l1 = 'псх'
counter = 1
f= 0
for a in l:
    for b in l:
        for c in l:
            for d in l:
                for f in l1:
                    w = a+b+c+d+f
                    print(w,counter)
                    if w == 'успех':
                        print(counter,w)
                        f = 1
                        break
                    counter += 1
                if f == 1:
                    break
            if f == 1:
                break
        if f == 1:
            break
    if f == 1:
        break
