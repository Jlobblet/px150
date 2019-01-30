import math
G,M,R = 6.67*10**-11,5.97*10**24,6371
def satellite(T):
	try:
		if T > 0:
			r = (G*M*(T**2)/4/(math.pi**2))**(1/3) - (R * 1000)
			if r > 0:
				return r
	except:
		pass