import sys
import numpy as np


def make_board(n):
    return np.array([[1 if x % 2 == 1 else 0 for x in range(1,n + 1)] if _ % 2 == 1 else [0 if x % 2 == 1 else 1 for x in range(1,n + 1)] for _ in range(1, n + 1)],dtype='int8')


print(make_board(7))
