def f(x,p):
    if (p == 5 or p == 3) and x <= 10:
        return 1
    if (p != 3 and p!=5 and x <= 10) or (p == 5 and x > 10):
        return 0
    if p % 2 == 0:
        return any([f(x//3,p+1),f(x-10,p+1)])
    else:
        return all([f(x // 3, p + 1), f(x - 10, p + 1)])

for i in range(11,10000):
    if f(i,1):
        print(i)




'''
33
34
35
36
37
38
39
40
41
42
=========================
53
54
55                 20 !!!!!!!!!!!!!
56
57
58
59
60
61
62
129
130
131
132
133
134
135
136
137
138
========================

33
34
35
36
37
38
39
40
41
42

        '''