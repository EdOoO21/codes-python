a = [int(x) for x in open('17 (9).txt')]

minv = 9999999999999
for i in a:
    if len(str(i)) == 3 and len(set(str(i))) == len(str(i)):
        minv = min(i,minv)
ans = []
print(minv)
for i in range(2500):

    if (a[i] * a[4999 - i]) % minv == 0:
        ans.append(a[i] + a[4999-i])
    print(i,4999-i)

print(len(ans),min(ans))