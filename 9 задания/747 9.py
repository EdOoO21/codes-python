f = open('747 9.txt')
counter = 0
for i in range(5000):
    ans = sorted(list(map(int, f.readline().split())))
    if len(set(ans)) == len(ans):
        if ((ans[0] + ans[4]) / 2) == ((ans[1] + ans[3]) / 2) == ans[2]:
            counter += 1
print(counter)
