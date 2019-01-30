def every_other(lis):
    r = list(())
    for i in range(len(lis)):
        if i%2 == 1:
            r.append(lis[i])
    return r