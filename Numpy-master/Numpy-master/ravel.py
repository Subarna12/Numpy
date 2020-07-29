import numpy as np

a = np.zeros(8)
arr3d = a.reshape((2,2,2))
#remember double brackets in zeros and reshape
arr = arr3d.ravel()
print(arr)