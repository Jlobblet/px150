def cumulative_sum(lis):
    j = 0
    r = list(())
    for i in range(len(lis)):
        j += lis[i]
        r.append(j)
    return r