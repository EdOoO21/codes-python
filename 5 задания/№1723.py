p = 14
for i in range(28,100):
    if p % 10 == i % 10 \
        or p//10==i//10\
        or p%10==i//10\
        or p//10==i%10:
        print(i,p)
    p+=1