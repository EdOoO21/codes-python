l = 'агилморт'
counter = 1
for a in l:
    for b in l:
        for c in l:
            for d in l:
                w = a + b + c + d
                print(w,counter)
                if 'им' in w:
                    print(counter,'==========================================================')
                counter += 1

