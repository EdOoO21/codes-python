s = [0]*1000
k = 0
for i in range(1000):
    s[i] = int(input())
for i in range(1000):
    for n in range(i+11,1000):
        if s[i] + s[n]<200:
            k+=1

print(k)

