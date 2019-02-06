import numpy as np
from math import sin,cos

def rotate2d(x,rad):
    rotate = np.array(([cos(rad),-sin(rad)],[sin(rad),cos(rad)]))
    return np.transpose(np.matrix(np.array(np.matmul(rotate,x))))