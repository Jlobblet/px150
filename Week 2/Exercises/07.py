import math
def mygauss(x,m,s):
    try:
        if s <=0:
            raise Error
        return (1/s/(2*math.pi)**0.5)*math.exp(-0.5*((x-m)/s)**2)
    except:
        pass