import numpy as np
def MCint_pi(n):
    M = 0
    for i in range(n):
        if ((np.random.random()*2-1)**2 + (np.random.random()*2-1)**2)**0.5 <= 1: M += 1
    return 4*M/n