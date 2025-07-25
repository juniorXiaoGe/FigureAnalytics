import numpy as np


ary1=np.arange(1,19)
print(ary1)


print(ary1.size)

ary1.shape=(2,9)
print(ary1)
print('-----------------------------')

ary1=ary1.reshape(9,2)
print(ary1)


ary1.resize(2,3,3)


print(ary1)
ary1.ravel()
print(ary1)