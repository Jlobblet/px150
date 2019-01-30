import math
def estimate_pi():
	recip = 0
	scalar = 2*(math.sqrt(2))/9801
	lastsum = 1
	k = 0
	while lastsum > 10e-5:
		lastsum = math.factorial(4*k) * (1103 + 26390 * k) / (math.factorial(k)**4) / 396**(4*k)
		recip += lastsum
		k += 1
	recip = recip * scalar
	pi = 1/recip
	return pi