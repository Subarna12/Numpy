import numpy as np

arr = np.arange(20)
arr_slice = slice(1,10,2)
print(arr[2:])
print(arr[:15])
#print(arr[0:2.2:0]) for just multidimensional arrays
print(arr[arr_slice])