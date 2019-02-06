import math
from scipy.integrate import quad

Gaussian = lambda x,m,s : (1/(2*math.pi)**0.5/s)*math.exp(-0.5*((x-m)/s)**2)

def myerror_function(L,U,m,s):
    return quad(Gaussian,L,U,args=(m,s))