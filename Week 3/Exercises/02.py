def slice_between(lis,start,end):
    try:
        if start > len(lis) or start > end:
            raise ValueError
        return lis[max(start,0):min(end,len(lis))]
    except:
        pass