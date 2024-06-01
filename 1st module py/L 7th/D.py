import sys
import numpy as np


def snake(M, N, direction='H'):
    if direction == 'H':
        return np.array([[((_ - 1) * M + x) for x in range(1, M + 1)] if _ % 2 == 1 else [((_ - 1) * M + x) for x in range(1, M + 1)[::-1]] for _ in range(1, N + 1)], dtype='int16')

    return np.array([[(((x-1)*N) + _) if x % 2 == 1 else (((x-1)*N) + (N - _ + 1)) for x in range(1, M + 1)] for _ in range(1, N + 1)], dtype='int16')


print(snake(5, 3))
