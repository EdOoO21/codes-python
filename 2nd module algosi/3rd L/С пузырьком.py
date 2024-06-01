from random import randint

n = int(input())
numbers = list(map(int, input().split()))
amount_of_swaps = 0

for i in range(n - 1):
    for k in range(n - 1 - i):
        if numbers[k] > numbers[k + 1]:
            numbers[k], numbers[k + 1] = numbers[k + 1], numbers[k]
            amount_of_swaps += 1
print(amount_of_swaps)