import numpy as np
def sunspots(flnm, r):
	x,y = np.loadtxt(flnm,unpack=True)
	return np.column_stack((x,np.convolve(y,np.ones((2*r+1))/(2*r),mode="same")))#78.5674
	
print(sunspots("sunspots.txt",15)[16][1])