import numpy as np

def off_diagonal(arr):
    r = list(())
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j > i: r.append(arr[i][j])
    return np.array(r)