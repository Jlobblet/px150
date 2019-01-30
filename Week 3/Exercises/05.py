def odd(inte):
    i = 0
    if inte % 2 == 0:
        inte -= 1
    while i <= inte:
        if i % 2 == 1:
            print(i)
        i += 1