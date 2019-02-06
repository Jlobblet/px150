import numpy as np

def diagonal(arr):
    r = list(())
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j: r.append(arr[i][j])
    return np.array(r)