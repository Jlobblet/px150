import numpy as np
def polyfit_file(flnm,degree):
    x,y = np.loadtxt(flnm,unpack=True)
    return np.polyfit(x,y,degree)