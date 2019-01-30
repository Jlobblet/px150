def nonzero_np(array):
    r = list(())
    for i in array:
        if i != 0:
            r.append(i)
    return np.array(r)