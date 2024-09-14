l = open('C:/Users/arbag/Desktop/файлы python/0901 24.txt')
l = l.readline()
l = l.replace('AAA','*')
l = l.replace('CCC','*')
l = l.replace('BBB','*')
l = l.replace('DDD','*')
l = l.replace('EEE','*')
l = l.replace('FFF','*')

s = []
counter = 0
print(l)
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        counter += 1
    else:
        s.append(counter)
        counter = 0

print(max(s))


