def odd_store(inte):
    r = list(())
    i = 0
    while i <= inte:
        if i % 2 == 1:
            r.append(i)
            if (i+1) == inte:
                break
        i += 1  
    return r