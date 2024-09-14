f = open('26_7602 (1).txt')
n = int(f.readline())
n1212 = int(f.readline())
pas = [[0, 0] for _ in range(n1212)]
for i in pas:
    i[0], i[1] = list(map(int, f.readline().split()))
print(pas)
pas.sort()
print(pas)
ans = [0] * n
f = 0
for i in pas:
    print(ans)
    for n in range(len(ans)):
        if ans[n] < i[0]:
            ans[n] = i[1]
            f += 1
            print(ans.index(i[1]))
            break
    

print(f)
