import sys
import numpy as np
def multiplication_matrix(n):
    return np.array([[x*_ for x in range(1,n+1)]for _ in range(1,n+1)])

print(multiplication_matrix(5))

