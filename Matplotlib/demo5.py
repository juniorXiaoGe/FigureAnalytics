'''子图：网格式布局'''
import matplotlib.pyplot as mp
mp.figure("gridspec",facecolor="green")
#构建三行三列的结构
mg = mp.GridSpec(3,3)

#第一个子图
mp.subplot(mg[0,0:2])#0第一行，  0:2从第一列切到第三列，不包括第三列
mp.text(0.5,0.5,1)
mp.xticks([])
mp.yticks([])
#第二个子图
mp.subplot(mg[0:2,2])#0:2表示切出前两行  2表示第三列
mp.text(0.5,0.5,2)
mp.xticks([])
mp.yticks([])
#第三个子图
mp.subplot(mg[1,1])#1表示第二行， 1表示第二列
mp.text(0.5,0.5,3)
mp.xticks([])
mp.yticks([])
#第四个子图
mp.subplot(mg[1:,0])#1:表示从第二行切到尾，  0表示第一列
mp.text(0.5,0.5,4)
mp.xticks([])
mp.yticks([])
#第五个子图
mp.subplot(mg[2,1:])#2表示第三行， 1：表示从第二列切到尾
mp.text(0.5,0.5,5)


mp.xticks([])
mp.yticks([])

mp.show()