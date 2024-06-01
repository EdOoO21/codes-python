from random import randint
def quicksort(line):
    if len(line) >= 2:
        oporn = line[randint(0,len(line) - 1)]
        more = [i for i in line if i > oporn]
        less = [i for i in line if i < oporn]
        equal = [i for i in line if i == oporn]
        return quicksort(less) + equal + quicksort(more)
    else:
        return line


n = int(input())
line1 = list(map(int, input().split()))

print(*quicksort(line1))