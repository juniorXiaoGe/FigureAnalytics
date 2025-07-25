import numpy as np
data1=[1,2,3,4,5]
data2=[1,2,3,4,5]
data=np.array([data1,data2])
print("改之前的数组形状为:")
print(data.shape)
data=data.reshape((5,2))
print("改之后的数组形状为:")
print(data.shape)