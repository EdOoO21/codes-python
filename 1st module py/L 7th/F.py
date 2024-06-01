import sys
import numpy as np


def manhattan_distance(point1, point2):
    return np.int32((abs(point1[0] - point2[0])) + (abs(point1[1] - point2[1])))


a = np.array([1, 2])
b = np.array([3, 4])
print(abs(a[0] - b[0]) + abs(a[1] - b[1]))
print(type(manhattan_distance(a, b)))
