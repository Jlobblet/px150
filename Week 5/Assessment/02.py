import numpy as np

def lorentz_test(mat):
	try:
		if mat.shape[0] != mat.shape[1] or not np.isclose(1,np.linalg.det(mat),rtol=0.01): return False
		m = list(())
		for i in range(len(mat)):
			r = list(())	
			for j in range(len(mat)):
				if i == j:
					if i == 0: r.append(-1)
					else: r.append(1)
				else: r.append(0)
			m.append(r)
		minkowski = np.mat(m)
		at = np.transpose(mat)
		test = np.matmul(at,np.matmul(minkowski,mat))
		if np.allclose(minkowski,test,rtol=0.01,atol=0.01): return True
		else: return False
	except:
		return False
