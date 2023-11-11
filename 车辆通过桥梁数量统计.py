# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:38:48 2023
多项式拟合实现估计
@author: 张启元
"""


import numpy as np

#单位时间内通行车数量
data_speed = [2, 2, 0, 2, 5, 8, 25, 12, 5, 10, 12, 7, 9, 28, 22, 10, 9, 11, 8, 9, 3]

#时间间隔
time_gap = [0, 120, 240, 300, 360, 420, 480, 540, 630, 690, 750, 840, 960, 1020, 1080, 1140, 1200, 1260, 1320, 1380, 1440]

#4次多项式拟合 , 得到多项式拟合系数
fit_4 = np.polyfit(time_gap, data_speed, 4)

#创建待拟合函数间隔
new_time_gap = range(0, 24*60)

#拟合值
fit_4_value = np.polyval(fit_4,new_time_gap)

#通过车辆总数
total_num = int(np.sum(fit_4_value))

print(total_num)