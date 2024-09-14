def F1(n):
    print(n)
    if n < 6:
        print(n)
        F1(n+1)
        F1(n+2)
        F1(n*2)

F1(1)

s = [0]*93

for i in range(len(s)):
    s[i] = int(input())

print(sum(s))