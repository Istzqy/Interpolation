# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:29:48 2023

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 定义二阶非线性微分方程
def model(y, t):
    y1, y2 = y
    dy1dt = y2
    dy2dt = -0.1 * y2 - np.sin(y1)
    return [dy1dt, dy2dt]

# 定义初始条件和时间间隔
y0 = [0.1, 0.0]  # 初始位移和初始速度
t = np.linspace(0, 50, 1000)  # 时间间隔从0到50，将其均匀分成1000个点

# 求解微分方程
y = odeint(model, y0, t)

# 绘制结果
plt.plot(t, y[:, 0], 'b', label='y(t)')  # 画出位移随时间的变化
plt.plot(t, y[:, 1], 'g', label='dy/dt(t)')  # 画出速度随时间的变化
plt.xlabel('Time')
plt.ylabel('Solution')
plt.title('Solution of Nonlinear ODE')
plt.legend()
plt.grid(True)
plt.show()
