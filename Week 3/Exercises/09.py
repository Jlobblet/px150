def average_odd_even(inte):
    if inte < 1:
        return
    oddList = list(())
    i = 0
    while i <= inte:
        if i % 2 == 1:
            oddList.append(i)
            if (i+1) == inte:
                break
        i += 1      
    evenList = oddList.copy()
    for i in range(len(evenList)):
        evenList[i] -= 1
    cycle = zip(oddList,evenList)
    sumList = list(())
    for i in cycle:
        sumList.append(i[0]+i[1])
    j = 0    
    for i in sumList:
        j += i
    j = j / len(sumList)
    return j