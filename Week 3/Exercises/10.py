def nearest_neighbours(inte):
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
    R = list(())
    for i in r:
        R.append(list((i-1,i+1)))
    return R