import numpy as np

a = np.array([(1,2,3),(4,5,6)])

print(a.max())
print(a.min())
print(a.sum())
print(a.sum(axis=1))
print(a.sum(axis=0))
print("--------------------------------------------")
print(np.sqrt(a))
print(np.std(a))
print("---------------------------------------------")
print(a.ndim)
print(a.itemsize)
print(a.dtype)
print(a.size)
print(a.shape)
print("----------------------------------------------")
a = a.reshape(3,2)
print(a)
print(a[0:,1])
a = np.linspace(1,3,10)
print(a)