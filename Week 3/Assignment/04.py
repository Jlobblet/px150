import math
g,y0 = 9.81,0
def trajectory(xdata,speed,angle):
	lis = list(())
	angle = math.radians(angle)
	fx = 0
	for x in xdata:
		fx = x*math.tan(angle) - (1/(2*speed**2))*(g*x**2)/(math.cos(angle))**2 + y0
		if fx >= 0:
			lis.append(fx)
	return lis