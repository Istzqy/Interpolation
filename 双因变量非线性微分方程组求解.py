# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:40:34 2023
求解三阶非线性微分方程组，含有两个因变量
@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 定义含两个因变量的二阶非线性微分方程
def model(y, t):
    y1, y2, y3, y4, y5 = y
    dy1dt = y2
    dy2dt = y3
    dy3dt = -3*y1*y3+2*y1**2-y4
    dy4dt = y5
    dy5dt = -2.1*y1*y5
    return [dy1dt, dy2dt, dy3dt, dy4dt, dy5dt ]

# 定义初始条件和时间间隔
y0 = [0, 0.0, 0.68, 1, -0.5]  # 初始位移、初始速度、初始位移、初始速度
t = np.linspace(0, 10, 1000)  # 时间间隔从0到50，将其均匀分成1000个点

# 求解微分方程
y = odeint(model, y0, t)

#创建图表和轴对象
fig, ax1 =plt.subplots()

#绘制第一个数据集（左Y轴）
ax1.plot(t,y[:, 0],'b-',label = 'f(η)')
ax1.set_xlabel('η')
ax1.set_ylabel('f(η)',color = 'b')
ax1.tick_params('y', colors = 'b')
#绘制第二个数据集
ax2 = ax1.twinx()
ax2.plot(t, y[:, 3], 'c', label='T(η)')
ax2.set_ylabel('T(η)',color = 'c')
ax2.tick_params('y',colors = 'c')
#添加图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper center')
plt.savefig('Imag/微分方程组数值解曲线.jpg', dpi=600)
plt.show()



# 绘制结果
# plt.plot(t, y[:, 0], 'b', label='y1(t)')  # 画出y1随时间的变化
# #plt.plot(t, y[:, 1], 'g', label='y2(t)')  # 画出y2随时间的变化
# #plt.plot(t, y[:, 2], 'r', label='y3(t)')  # 画出y3随时间的变化
# plt.plot(t, y[:, 3], 'c', label='y4(t)')  # 画出y4随时间的变化
# plt.xlabel('Time')
# plt.ylabel('Solution')
# plt.title('Solution of Nonlinear ODE with 2 Dependent Variables')
# plt.legend()
# plt.grid(True)
# plt.show()




