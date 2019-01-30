def odd_to_even(lis):
    r = lis.copy()
    for i in range(len(r)):
        r[i] -= 1
    return r