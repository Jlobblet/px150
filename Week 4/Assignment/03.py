import numpy as np
def rolling_dice(N,f):
    if N > 1e6: return
    r = 0
    for i in range(int(N)):
        if np.random.randint(1,7) == f and np.random.randint(1,7) == f: r += 1
    return r

def test_throw(N,f):
    try:
        if not f in range(1,7) or not N in range(1,1000001) or type(f) != int: raise ValueError
        R = rolling_dice(N,f)
        return R/N
    except:
        pass