import numpy as np
def die_series(n,f):
    streak = 0
    r = 0
    for i in range(n):
        if np.random.randint(1,7) == f:
            streak += 1
            if streak >= 3:
                r += 1
        else:
            streak = 0
    return r/n