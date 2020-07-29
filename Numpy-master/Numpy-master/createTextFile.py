import numpy as np

arr = np.arange(20)
print(arr)
np.savetxt('testFile.txt', arr)
new_arr = np.loadtxt('testFile.txt')
print(new_arr)