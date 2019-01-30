import numpy as np
def biased_coin(n):
    heads = 0
    for i in range(n):
        if np.random.random() <= 0.2:
            heads += 1
    return heads/n