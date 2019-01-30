def nearest_neighbours_dict(inte):
    if inte < 1:
        return
    r = list(())
    i = 0
    while i <= inte:
        if i % 2 == 1:
            r.append(i)
            if (i+1) == inte:
                break
        i += 1
    R = dict(())
    for i in range(len(r)):
        R[2*i + 1] = list((r[i]-1,r[i]+1))
    return R   