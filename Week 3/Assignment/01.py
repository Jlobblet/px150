def mysum(lis):
		if isinstance(lis,dict):
			s = 0
			for i in lis.values():
				s += i
			return s
		else:
			try:
				s = 0
				for i in lis:
					s += i
				return s
			except:
				pass