from scipy.integrate import quad

def area_line(L,U,a,b):
    def integrand(x): return a*x+b
    return quad(integrand,L,U)