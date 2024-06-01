from collections import deque

first = deque((map(int, str(input()).split())))
second = deque((map(int, str(input()).split())))
step_amount = 0
while (len(first) != 0) and (len(second) != 0):
    step_amount += 1
    if (first[0] == 9) and (second[0] == 0):
        second.append(first[0])
        second.append(second[0])
        second.popleft()
        first.popleft()
    elif (first[0] == 0) and (second[0] == 9):
        first.append(first[0])
        first.append(second[0])
        second.popleft()
        first.popleft()
    elif first[0] < second[0]:
        second.append(first[0])
        second.append(second[0])
        second.popleft()
        first.popleft()
    elif first[0] > second[0]:
        first.append(first[0])
        first.append(second[0])
        second.popleft()
        first.popleft()

if not first:
    print(f'second {step_amount}')
else:
    print(f'first {step_amount}')
