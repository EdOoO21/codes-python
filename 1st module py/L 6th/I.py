from itertools import product

s = str(input())
a = ['пик', 'треф',  'бубен', 'червей']
a.remove(s)
b = [x for x in range(2, 11)]
b += ['валет', 'дама', 'король', 'туз']
for i in product(b, a):
    print(*i)
