import math
def p2c(r,theta):
	try:
		if r <= 0:
			raise Error
		return (r*math.cos(math.radians(theta)),r*math.sin(math.radians(theta)))
	except:
		pass