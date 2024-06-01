import sys
import numpy as np

def rotate(np_array, angle):
    return np.rot90(np_array,-angle/90)

print(rotate(np.arange(12).reshape(3, 4), 270))

