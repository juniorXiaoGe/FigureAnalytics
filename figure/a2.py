import numpy as np
data1=np.arange(1,6)
data2=np.arange(6,11)
data=np.array([data1,data2])
print("改之前的数组形状为:")
print(data.shape)
data=data.reshape((5,2))
print("改之后的数组形状为:")
print(data.shape)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")

data3=np.vstack((data1,data2))
print(data3)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
data4=np.hstack((data1,data2))
print(data4)
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
data4=np.dstack((data1,data2))
print(data4)



data = np.array([1,2,3])
print(data.ndim)
print(data.dtype)