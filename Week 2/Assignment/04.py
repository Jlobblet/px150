m,V,h = 511*10**3,9,4.135667
def trprob(E):
	try:
		if E >= V:
			k1 = (2*m*E)**0.5/h
			k2 = (2*m*(E-V))**0.5/h
			T = 4*k1*k2/(k1+k2)**2
			R = ((k1-k2)/(k1+k2))**2
			return (T,R)
	except:
		pass