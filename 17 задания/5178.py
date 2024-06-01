a = [int(x) for x in open('C:/Users/arbag/Desktop/78.txt')]

counter = 0
s = []
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) % 11 == 0:
        counter += 1
        s.append(a[i] + a[i+1])

print(counter,max(s))
