def mymin(lis):
    j = lis[0]
    for i in lis:
        if i < j:
            j = i
    return j