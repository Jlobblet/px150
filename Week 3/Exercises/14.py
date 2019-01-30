import math
def sqrt_Newton(a,x): #import math
    y = 0
    while True:
        y = (x + (a/x))/2
        if abs(y - math.sqrt(a)) <= 1e-5:
            break
        x = y
    return tuple((y,math.sqrt(a)))