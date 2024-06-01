import sys
from functools import reduce
from itertools import product


def generate_sequences(n, a):
    l = reduce(lambda x, y: str(x) + str(y), range(0, a))

    for i in product(l, repeat=n):
        yield ''.join(i)

exec(sys.stdin.read())

for seq in generate_sequences(2, 3):
    print(seq.replace("", " ")[1:-1])
