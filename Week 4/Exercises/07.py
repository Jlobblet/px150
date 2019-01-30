import numpy as np
def single_die(n,f):
    r = 0
    for i in range(n):
        if np.random.randint(1,7) == f:
            r += 1
    return r/n