# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:38:48 2023
线性插值实现估计
@author: admin
"""

from scipy.interpolate import interp1d
import numpy as np


#单位时间内通行车数量
data_speed = [2, 2, 0, 2, 5, 8, 25, 12, 5, 10, 12, 7, 9, 28, 22, 10, 9, 11, 8, 9, 3]

#时间间隔
time_gap = [0, 120, 240, 300, 360, 420, 480, 540, 630, 690, 750, 840, 960, 1020, 1080, 1140, 1200, 1260, 1320, 1380, 1440]

#线性插值计算插值函数
interpolta_fuc = interp1d(time_gap, data_speed, kind='linear')

#新间隔
new_time_gap = range(0,24*60)
#估计值
estimated_value =  interpolta_fuc(new_time_gap)

#通过车辆总数
total_num = int(np.sum(estimated_value))
print(total_num)