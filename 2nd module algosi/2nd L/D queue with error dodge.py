from collections import deque
queue = deque()
n = str(input()).split()
while n[0] != 'exit':
    if n[0] == 'push':
        queue.append(n[-1])
        print('ok')
    elif (n[0] == 'pop') and (len(queue) > 0):
        print(queue[0])
        queue.popleft()
    elif (n[0] == 'pop') and (len(queue) == 0):
        print('error')
    elif (n[0] == 'front') and (len(queue) > 0):
        print(queue[0])
    elif (n[0] == 'front') and (len(queue) == 0):
        print('error')
    elif n[0] == 'size':
        print(len(queue))
    elif n[0] == 'clear':
        queue = deque()

        print('ok')
    n = str(input()).split()
print('bye')