import numpy as np
def flip_coin(N):
    if N > 1e6:
        return
    r = 0
    for i in range(int(N)):
        if np.random.randint(1,3) == 1:
            r += 1
    return r