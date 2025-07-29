import matplotlib.pyplot as plt
import numpy as np
# #画一条线
# x = np.array([4,10])#所有的点的x坐标组成的数组
# y = np.array([15,25])#所有的点y坐标组成的数组
#
# #画
# # mp.plot(x,y,linestyle=":",
# #         linewidth=2.2,color="gold",alpha=0.2)
#
#
# plt.plot([1,2,3])
# plt.subplot(233)
# plt.subplot(213)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# ypoints = np.array([3, 10,121,32,1,322,2])
#
# plt.plot(ypoints, marker = 'o',ms = 20)
# plt.grid()
# plt.show()

#plot 1:
xpoints = np.array([0, 6])
ypoints = np.array([0, 100])

plt.subplot(2, 2, 1,index=1)
plt.plot(xpoints,ypoints)
plt.title("plot 1")

#plot 2:
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

plt.subplot(2, 2, 3)
plt.plot(x,y)
plt.title("plot 2")

plt.suptitle("RUNOOB subplot Test")
plt.show()