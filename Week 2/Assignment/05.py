import math
G,M = 6.67*10**-11,1.9891*10**30
def orbit(l1,v1):
    quada = 1
    quadb = -2*G*M/l1/v1
    quadc = -1*(v1**2-(2*G*M/l1))
    v2 = (-quadb - math.sqrt(quadb**2-4*quada*quadc))/(2*quada)
    l2 = l1*v1/v2
    a = 0.5*(l1+l2)
    b = (l1*l2)**0.5
    T = 2*math.pi*a*b/l1/v1
    e = (l2-l1)/(l2+l1)
    return (a,b,T,e)