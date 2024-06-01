s=1
for i in range(2532000,2532161):
    count=0
    for n in range(2,(i//2)+1):
        if i % n == 0:
            count+=1
            break
    if count == 0 and i % 10 == 3:
        print(s,i)
        s+=1
