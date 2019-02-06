import numpy as np

def lorentz_test(mat):
    try:
        if mat.shape[0] != mat.shape[1] or np.linalg.det(mat) != 1: return False
        minowski = np.matrix(np.array(((np.array([1,0,0,0]),np.array([0,-1,0,0]),np.array([0,0,0,-1]),np.array([0,0,0,-1])))))
        at = np.transpose(mat)
        test = np.matmul(at,np.matmul(minowski,mat))
        if test[0][0] <= 0.99 or test[0][0] >= 1.01 or test[1][1] <= -1.01 or test[1][1] >= -0.99 or test[2][2] <= -1.01 or test[2][2] >= -0.99 or test[3][3] <= -1.01 or test[3][3] >= -0.99: return False 
        return True
    except:
        return False

print(lorentz_test(np.matrix(np.array(((np.array([1,0,0,0]),np.array([0,-1,0,0]),np.array([0,0,0,-1]),np.array([0,0,0,-1])))))))