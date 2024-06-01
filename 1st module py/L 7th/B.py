import sys
import numpy as np
def get_det_matrix(a):
    return np.linalg.det(a)


a = np.array([[1,2],[3,4]])
print(int(get_det_matrix(a)))
