def find_neighbour_lists(lis,inte):
    if len(lis) < int(inte/2) or inte % 2 == 0:
        return
    for i in lis:
        if i[0] == inte - 1 and i[1] == inte + 1:
            return tuple((inte-1,inte+1))
            break