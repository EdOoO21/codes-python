from collections import deque


def push_front(deque, num):

    deque.appendleft(num)
    print('ok')


def push_back(deque, num):
    deque.append(num)
    print('ok')


def pop_front(deque):
    if len(deque) == 0:
        print('error')
    else:
        print(deque.popleft())


def pop_back(deque):
    if len(deque) == 0:
        print('error')
    else:
        print(deque.pop())


def back(deque):
    if len(deque) == 0:
        return 'error'
    return deque[-1]


def front(deque):
    if len(deque) == 0:
        return 'error'
    return deque[0]


def size(deque):
    return len(deque)


def clear(deque):
    deque.clear()
    return deque


def exit():
    print('bye')
    return

dq = deque()
print(size(dq))
push_back(dq, 1)
print(size(dq))
push_back(dq, 2)
print(size(dq))
push_front(dq, 3)
print(size(dq))
exit()

