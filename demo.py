import numpy as np


frame = np.random.rand(64,64,3)
mask = np.ones((64,64))

k = frame[frame>0.2]  #把frame中所有符合条件的元素输出，k为一维array

frame_r,frame_g,frame_b = frame[:,:,0].copy(),frame[:,:,1].copy(),frame[:,:,2].copy()

#对三个通道分量进行筛选，如果某个位置的三个通道中有一个通道不符合条件，
# 则把它对应的mask上的元素置零。最后得到mask矩阵，值为1的地方就是符合条件的地方
mask[frame_r <0.1] = 0
mask[frame_r >0.8] = 0
mask[frame_g <0.2] = 0
mask[frame_g >0.7] = 0
mask[frame_b <0.1] = 0
mask[frame_b >0.9] = 0

#把mask矩阵所有值为1的元素的位置输出。
#比如location_x = array([0,0,2,3])
#location_y = array([1,2,3,5])
#那么意味着mask矩阵中元素为1的位置为(0,1),(0,2),(2,3),(3,5)
location_x,location_y = np.where(mask!=0)
