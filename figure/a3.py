import numpy as np
'''电信用户行为数据分析'''
#(4975,7)
#id编号，pack_type:套餐的类型 extra_time：剩余的通话时长
# pack_change：是否更改套餐
#contract:欠费与否
#extra_flow:剩余流量
# Loss:流失与否
data=[]
with open("Customer_data.csv") as f:
    lines = f.readlines()
    #enumerate内置函数,可以迭代出索引以及数据
    for index,line in enumerate(lines):
        if index == 0:#表示是第一行
            pass
        else:
            print(index, line)
            data.append(line[:-1].split(","))

ary = np.array(data,dtype="f8")
#进行具体的每一列的分析
#求剩余流量 剩余通话的均值
extra_flow = ary[:,3]#得到剩余流量列,是一个一维的
extra_time = ary[:,2]#得到剩余通话列,是一个一维的
print("剩余流量的最小值:",min(extra_flow))
print("剩余流量的最大值:",max(extra_flow))
print("剩余流量的均值:",np.mean(extra_flow))

#有剩余流量的人的占比,  掩码, 内置len(extra_flow)

#统计每一个套餐的人数在总人数中的占比,掩码